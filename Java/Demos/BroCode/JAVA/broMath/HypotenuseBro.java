package broMath;
import java.util.Scanner;

// Finding the hypotenuse of a triangle.

public class HypotenuseBro {

    public static void main(String[] args) {

        double x;
        double y;
        double z;

        Scanner Scanner = new Scanner(System.in);

        System.out.println("Enter the value of x:");
        x = Scanner.nextDouble();
        // nextDouble() method scans the next token of the input as a double.

        System.out.println("Enter the value of y:");
        y = Scanner.nextDouble();
        System.out.println("Enter the value of z:");

        z = Math.sqrt((x * x) + (y * y));
        /**
         * The length of the hypotenuse can be found using the
         * Pythagorean theorem, which states that the square of
         * the length of the hypotenuse equals the sum of the
         * squares of the lengths of the other two sides.
         */

        System.out.println("The Hypotenuse is " + z);

        Scanner.close();
    }
}

// * Java Math class
// https://www.youtube.com/watch?v=w0VTlSOXBs8&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=7