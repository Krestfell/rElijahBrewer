/**
 * bankinvestment
 */
public class bankinvestment {

    public static void main(String[] args) {
            int year =0;
            double interest;
            double balance = 10000;
            double percent = .05;
            while (balance < 20000)
            {
                year = year + 1;
                interest = balance * percent;
                balance = balance + interest;
            }
            System.out.println("Number of years is " + year);
    }
}