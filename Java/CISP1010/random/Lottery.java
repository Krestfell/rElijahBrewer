import java.util.Scanner;

public class Lottery {

    public static void main(String[] args) {
        // Generates lottery
        int lottery = (int) (Math.random() * 100);

        // Ask user for their guess
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your Lottery Number (two digits)");
        int guess = input.nextInt();

        // Get digits from lottery
        int lotteryDigit1 = lottery / 10;
        int lotteryDigit2 = lottery % 10;

        // Get digits from guess
        int guessDigit1 = guess / 10;
        int guessDigit2 = guess % 10;

        System.out.println("The Lottery Number is " + lottery);

        // Check the guess
        if (guess == lottery)
            System.out.println("Exact match: You Win 10,000!");
        else if (guessDigit2 == lotteryDigit1
                && guessDigit1 == lotteryDigit2)
            System.out.println("All Digits Match: you win $3,000!");
        else if (guessDigit1 == lotteryDigit1
                || guessDigit1 == lotteryDigit2
                || guessDigit2 == lotteryDigit1
                || guessDigit2 == lotteryDigit2)
            System.out.println( "One Digit Matches: you win $1,000!");
        else
            System.out.println("No Match: you lose!");

    }

}