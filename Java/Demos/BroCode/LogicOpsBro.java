import java.util.Scanner;

public class LogicOpsBro {

    // logical operators = used to connect two or more expressions

    //

    // && = (AND) both conditions must be true

    // || = (OR) either condition must be true

    // . ! = (NOT) reverses boolean value of condition

    public static void main(String[] args) {

        // &&

        int temp = 81;

        if (temp > 80) {
            System.out.println("It's hot");
        } else if (temp >= 60 && temp <= 75) {
            System.out.println("It's warm");
        } else {
            System.out.println("It's cold");
        }

        // ||, !

        Scanner scanner = new Scanner(System.in);

        System.out.println("Press Q or q to quit");
        String response = scanner.next();

        if (!response.equals("Q") || !response.equals("q")) {
            System.out.println("You Quit");
        } else {
            System.out.println("You stayed");
        }
        scanner.close();
    }
}

// * Java logical operators (AND OR NOT)
// https://www.youtube.com/watch?v=919IUhotDCo&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=11