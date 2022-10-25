package WhileLoopDemo;

/**
 * WhileLoopDemo
 */
public class WhileLoopDemo {

    public static void main(String[] args) {

        int year = 0;
        double interest = 0;
        double balance = 10000;
        final double TARGET_BALANCE = 2 * balance;
        final double INTEREST_RATE = 0.05;

        while (balance < TARGET_BALANCE) {
            year++;
            interest = balance * INTEREST_RATE;
            balance += interest;
        }
        System.out.println("The total number of years is " + year);
        System.out.println("The interest = " + interest);
    }
}