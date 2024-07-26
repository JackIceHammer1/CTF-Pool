public class Writeup {

    // Upon starting the challenge, we get an extensionless file named enc and a
    // file named out.txt. Forensics shows us that the first is an ELF binary and
    // the second is a hexadecimal string encrypted in some manner. Decompiling the
    // ELF shows us the script that created the string in out.txt, doing so by
    // converting the flag to hexadecimal and then shifting both the numbers of the
    // hex forward by 3. Below is an example of a script to decrypt it.
    public static final String FLAG = "lbctf{h3re_it_1s}";

    // ------------------------------------------------------------------------\\
    // ------------------------------begin script------------------------------\\
    // ------------------------------------------------------------------------\\

    public static String encryptedString = "9f9596a799ae9b66a598829ca78264a6a0";//
    public static char[] hex = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f' };

    public static int findPosition(char[] chArr, char target) {
        for (int i = 0; i < chArr.length; i++) {
            if (chArr[i] == target) {
                return i;
            }
        }
        return -1;
    }

    public static String decrypt(String str) {
        StringBuilder temp = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            char current = str.charAt(i);
            int pos = findPosition(hex, current);
            int newPos = (pos - 3 + hex.length) % hex.length;
            temp.append(hex[newPos]);

        }
        return temp.toString();
    }

    public static void main(String[] args) {
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < encryptedString.length(); i += 2) {
            String hexPair = encryptedString.substring(i, i + 2);
            System.out.println(hexPair + " " + (char) Integer.parseInt(decrypt(hexPair), 16));
            output.append((char) Integer.parseInt(decrypt(hexPair), 16));
        }

        System.out.println(output);
    }
}