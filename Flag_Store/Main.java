import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int money = 1000;
        boolean playing = true;
        boolean flag = false;
        while (playing == true) {
            System.out.println("");
            System.out.println("0: Withdraw money ");
            System.out.println("1: Buy russian doll");
            System.out.println("2: Display account balance");
            System.out.println("3: Buy your flag");
            System.out.println("4: Quit");
            System.out.println("Select one of the options above (0-4): ");
            int response = input.nextInt();
            if (response == 0) {
                System.out.println("How much money would you like to withdraw? ");
                int withdraw = input.nextInt();
                money = money - withdraw;
                System.out.println("Your new balance is: " + money);
                System.out.println("");
            } else if (response == 1) {
                System.out.println("How many dolls would you like to buy? ($500 each)");
                int dollNum = input.nextInt();
                money = money - (500 * dollNum);
                System.out.println("Your new balance is: " + money);
                System.out.println("");
            } else if (response == 2) {
                System.out.println("Your balance is: " + money);
                System.out.println("");
            } else if (response == 3) {
                System.out.println("Would you like to buy your flag? (0: Yes, 1: No):");
                int flagResponse = input.nextInt();
                if (flagResponse == 0) {
                    if (money >= 1000000) {
                        System.out.println("Congrats! You will find your flag below.");
                        System.out.println("");
                        flag = true;
                        playing = false;
                    } else {
                        System.out.println("Sorry! You have no money loser. The flag is $1000000");
                        System.out.println("");
                    }
                } else if (flagResponse == 1) {
                    System.out.println("Okay.");
                    System.out.println("");
                } else {
                    System.out.println("Invalid Statement.");
                    System.out.println("");
                }

            } else if (response == 4) {
                playing = false;
            } else {
                System.out.println("Invalid Statement.");
                System.out.println("");
            }
        }
        if (flag == true) {
            System.out.println("lbctf{g3T_Ur_f1@g5}");
            // lbctf{g3T_Ur_f1@g5}
        }

    }

}
