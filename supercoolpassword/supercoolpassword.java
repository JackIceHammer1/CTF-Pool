import java.util.Scanner;

class Password 
{
    public static void main(String args[])
    {
        Password supercoolpassword = new Password();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter password: ");
        String userInput = scanner.next();
        String input = userInput.substring("lbctf{".length(), userInput.length()-1);
        if (supercoolpassword.checkPassword(input))
        {
            System.out.println("Access Granted.");
        } else {
            System.out.println("Access Denied!");
        }
    }


public boolean checkPassword(String password)
{
    byte[] passBytes = password.getBytes();
    byte[] myBytes = {
            100, 64, 95, 98, 51, 115, 0x54, 0x5f, 0x50, 0x40, 0x73, 0x73, 0x77, 0x30, 0x52, 0x64, 0x5f, 0x31, 0156, 0137, 0067, 0150, 0063, 0137, 0167, 0060, 0122, 0061, 0144
    };
    for (int i = 0; i<32; i++)
    {
        if (passBytes[i] != myBytes[i]) {
            return false;
        }
    }
    return true;

    
}
}
