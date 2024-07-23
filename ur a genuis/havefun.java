import java.util.Scanner;
public class havefun {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the key: ");
        String key = input.nextLine();
        input.close();
        String characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=_+[]{}|;':,.<>?/";
        String result = "";
        result = key.substring(key.length()-2, key.length()-1);
        result = result + characters.substring(key.length()-9,3) + "tf" + characters.substring(key.indexOf("i")+78, 79);
        result = result + characters.substring(key.length()+7, 18) + (key.indexOf("n")+2) + "@" + characters.substring(key.length()-7, 4) + key.substring(0,2) + "S";
        if(key.indexOf("e") > 7){
            result = result + "truct";
        }
        if(key.indexOf("I") > 2){
            result = result + "ions";
        }
        result = result + (11+key.indexOf("z")) + key.substring(1,2) + 5 + "}";
        String[] resultArray = new String[result.length()];
        for (int i = 0; i < result.length(); i++) {
            resultArray[i] = result.substring(i, i + 1);
        }
        for(int j = 0; j < resultArray.length; j++){
            System.out.println(resultArray[j]);
        }
    }
}



