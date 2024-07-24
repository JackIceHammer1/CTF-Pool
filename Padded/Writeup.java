/*
The description tells us that the image containing the flag was split into two parts.
Upon looking at the images we're given, they look like static.
Closer inspection shows that it's made up of a bunch of 2 pixel by 2 pixel squares, with black and white in a checkerboard pattern.
This implies to us that the images are one-time padded to each other.

Below is the script I wrote to generate them, along with a method that will decrypt them.

lbctf{0v3rl4pp1ng}
*/

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import java.util.concurrent.ThreadLocalRandom;

public class Writeup {
    public static final int BLACK = (255 << 24) | (0 << 16) | (0 << 8) | 0;
    public static final int WHITE = (0 << 24 | 255 << 16 | 255 << 8 | 255);

    public static void enc() {
        BufferedImage img = null;
        File f = null;

        try {
            // either put it in your working directory or define an absolute filepath
            f = new File("in.png");
            img = ImageIO.read(f);
        } catch (IOException e) {
            System.out.println(e);
        }
        int width = img.getWidth();
        int height = img.getHeight();
        // create two images each twice the size of in.png

        // out1:
        BufferedImage out1 = new BufferedImage(width * 2, height * 2, BufferedImage.TYPE_INT_RGB);
        // out2:
        BufferedImage out2 = new BufferedImage(width * 2, height * 2, BufferedImage.TYPE_INT_RGB);

        // anything we put inside the second for loop will iterate once for each pixel
        // in our original image
        for (int i = 0; i < width; i++) {
            for (int ii = 0; ii < height; ii++) {
                int color1;
                int color2;
                // get the color of the original pixel
                int color = img.getRGB(i, ii);
                // get the blue, green, and red
                int blue = color & 0xff;
                int green = (color & 0xff00) >> 8;
                int red = (color & 0xff0000) >> 16;
                boolean isBlack = (blue + green + red) / 3 <= 127;

                // decide randomly which formation to have so that we can't see a pattern
                if (ThreadLocalRandom.current().nextInt(0, 2) == 0) {
                    color1 = BLACK;
                    color2 = WHITE;
                } else {
                    color1 = WHITE;
                    color2 = BLACK;
                }
                out1.setRGB(2 * i, 2 * ii, color1);
                out1.setRGB(2 * i + 1, 2 * ii, color2);
                out1.setRGB(2 * i, 2 * ii + 1, color2);
                out1.setRGB(2 * i + 1, 2 * ii + 1, color1);
                if (isBlack) {
                    out2.setRGB(2 * i, 2 * ii, color2);
                    out2.setRGB(2 * i + 1, 2 * ii, color1);
                    out2.setRGB(2 * i, 2 * ii + 1, color1);
                    out2.setRGB(2 * i + 1, 2 * ii + 1, color2);
                } else {
                    out2.setRGB(2 * i, 2 * ii, color1);
                    out2.setRGB(2 * i + 1, 2 * ii, color2);
                    out2.setRGB(2 * i, 2 * ii + 1, color2);
                    out2.setRGB(2 * i + 1, 2 * ii + 1, color1);
                }
            }
        }

        // write the files
        File out1name = new File("out1.png");
        try {
            ImageIO.write(out1, "png", out1name);
        } catch (IOException e) {
            System.out.println(e);
        }
        File out2name = new File("out2.png");
        try {
            ImageIO.write(out2, "png", out2name);
        } catch (IOException e) {
            System.out.println(e);
        }
    }

    public static void dec() {
        BufferedImage in1 = null;
        BufferedImage in2 = null;
        File f = null;
        try {
            f = new File("out1.png");
            in1 = ImageIO.read(f);
            f = new File("out2.png");
            in2 = ImageIO.read(f);
        } catch (IOException e) {
            System.out.println(e);
        }
        int width = in1.getWidth();
        int height = in1.getHeight();
        // don't want to assume they're the same size
        if (width != in2.getWidth() || height != in2.getHeight()) {
            System.out.println("Error decrypting. Overlay images are not the same size.");
            return;
        }
        // check that the size will map properly
        if (width % 2 != 0 || height % 2 != 0) {
            System.out.println("Error decrypting. Overlay images are corrupted.");
            return;
        }

        // create the outfile
        BufferedImage out = new BufferedImage(width / 2, height / 2, BufferedImage.TYPE_INT_RGB);

        for (int i = 0; i < width / 2; i++) {
            for (int ii = 0; ii < height / 2; ii++) {
                // taking a shortcut here
                // instead of comparing every pixel of a 2x2 square, we only compare the top
                // left pixel
                // assumes that every 2x2 is in the format we're expecting; might make it
                // incompatible with other implementations
                // but it's an assumption that divides the running time by 4, which is relevant
                // for larger files

                // if top left pixel is the same, then we color the pixel of our outfile white;
                // otherwise, we color it black
                if (in1.getRGB(2 * i, 2 * ii) == in2.getRGB(2 * i, 2 * ii)) {
                    out.setRGB(i, ii, WHITE);
                } else {
                    out.setRGB(i, ii, BLACK);
                }
            }
        }

        // write the file
        File name = new File("decrypted.png");
        try {
            ImageIO.write(out, "png", name);
        } catch (IOException e) {
            System.out.println(e);
        }
    }

    public static void main(String[] args) throws IOException {
        // enc();
        dec();
    }
}