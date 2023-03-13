package broLoops;

import java.util.Scanner;

public class WhileLoopBro {

    // While loop: executes a block of code as long as it's condition is true.
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        String name = "";

        while (name.isBlank()) {
            System.out.print("Enter name");
            name = scanner.nextLine();
        }
        System.out.println("Hello " + name);
        // do while loop: replace first line with do and move line to end.

        scanner.close();
    }
}

// * Java while loop
// https://www.youtube.com/watch?v=t6gmQaTMTtM&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=12