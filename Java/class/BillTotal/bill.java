import java.util.Scanner;

/**
 * bill
 */
public class bill {

    public static void main(String[] args) {
       Scanner input = new Scanner(System.in);
        double tip =.15;
        double total;

         // Get number of people
        System.out.println("How many people are we dining with today? ");
        int people = input.nextInt();
        
        //Get bill total
        System.out.println("How much is the bill? ");
        double bill = input.nextDouble();

        total = (bill + (bill * tip)) / people;
        System.out.println("Your split total is " + total);
    }
}