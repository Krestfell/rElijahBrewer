package broStatements;
// Java user input scanner

import java.util.Scanner;

// * ^ Import is from a different package and must be imported.

/**
 * Import is a Java keyword.
 * It declares a Java class to use in the code
 * below or after the import statement.
 * Once a Java class is declared,
 * then the class name can be used in the code
 * without specifying the package the class belongs to.
 */

public class ScannerBro {
   public static void main(String[] args) {

      Scanner scanner = new Scanner(System.in);

      // * ^ Scanner: A class in java.util package.
      // Used for obtaining user input.

      System.out.println("What is your name? ");
      String name = scanner.nextLine();

      // * ^ nextLine(): A method of java.util.Scanner class.
      /**
       * Advances this scanner past the current line and returns
       * the input that was skipped. This function prints the
       * rest of the current line, leaving out the line separator
       * at the end.
       */

      System.out.println("How old are you? ");
      int age = scanner.nextInt();

      // * ^ nexInt(): A method of java.util.Scanner class.
      // Scans the next token of the input data as an int.

      scanner.nextLine();

      // ! ^ Using nextLine directly after nextInt will confuse the compiler.
      // A workaround is to use a blank nextLine to clear it.

      System.out.println("What is your favorite color? ");
      String color = scanner.nextLine();

      System.out.println("Hello, " + name);
      System.out.println("You are " + age + " years old");
      System.out.println("Your favorite color is " + color);

      scanner.close();

      // It's good practice to close your scanner when you are done using it.
   }
}

// * How to accept user input in Java
// https://www.youtube.com/watch?v=wAEPokhj5Q4&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=4