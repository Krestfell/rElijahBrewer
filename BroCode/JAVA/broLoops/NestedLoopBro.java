package broLoops;

import java.util.Scanner;

public class NestedLoopBro {

    // Nested loop: a loop inside of a loop.
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int rows;
        int columns;
        String symbol = "";

        System.out.println("Enter the number of rows");
        rows = scanner.nextInt();
        System.out.println("enter the number of columns");
        columns = scanner.nextInt();
        System.out.println("Enter the symbol to use");
        symbol = scanner.next();

        for (int i = 1; i <= rows; i++) {
            System.out.println();
            // Outer loop is in charge of rows

            for (int j = 1; j <= columns; j++) {
                System.out.print(symbol);
                // Inner loop is in charge of columns
            }
        }
    }
}

// * Java Nested Loops
// https://www.youtube.com/watch?v=oF3nBQFfpeM&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=14-