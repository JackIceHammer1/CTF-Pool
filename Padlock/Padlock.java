import java.util.*;

class Padlock {
    public static void main(String args[]) {
        Padlock vaultDoor = new Padlock();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
	String userInput = scanner.next();
	String input = userInput.substring("lbctf{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
	}
    }

    // 
    public boolean checkPassword(String password) {
        return password.length() == 19 &&
               password.charAt(0)  == 'l' &&
               password.charAt(4)  == 'f' &&
               password.charAt(2)  == 'c' &&
               password.charAt(3)  == 't' &&
               password.charAt(17) == 'r' &&
               password.charAt(1)  == 'b' &&
               password.charAt(7)  == 't' &&
               password.charAt(10) == 's' &&
               password.charAt(5)  == '{' &&
               password.charAt(9)  == 'a' &&
               password.charAt(11) == 'n' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'W' &&
               password.charAt(12) == 't' &&
               password.charAt(14) == 'e' &&
               password.charAt(6)  == 'I' &&
               password.charAt(18) == 'e' &&
               password.charAt(13) == 'S' &&
               password.charAt(19) == '?' &&
               password.charAt(16) == 'u' &&
               password.charAt(20) == '?' &&
               password.charAt(21) == '}';
    }
}
