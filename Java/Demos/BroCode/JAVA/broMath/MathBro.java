package broMath;
public class MathBro {

    public static void main(String[] args) {

        double x = 3.14;
        double y = 9;

        double z = Math.max(x, y);
        /**
         * The Math class contains methods for finding the
         * maximum or minimum of two values, rounding values,
         * logarithmic functions, square root, and trigonometric
         * functions
         */
        // max() function returns maximum of two numbers.

        double v = Math.min(x, y);
        // min() function returns minimum of two numbers.

        double i = Math.abs(y);
        // abs() function returns the absolute value of a number.

        double j = Math.sqrt(x);
        // sqrt() function returns the square root of a number.

        double k = Math.round(x);
        // round() function returns the rounded value of a number.

        double m = Math.ceil(x);
        // ceil() function returns the ceiling value of a number.

        double n = Math.floor(x);
        // floor() function returns the floor value of number.

        System.out.println(z);
        System.out.println(v);
        System.out.println(i);
        System.out.println(j);
        System.out.println(k);
        System.out.println(m);
        System.out.println(n);
    }
}

// * Java Math class
// https://www.youtube.com/watch?v=w0VTlSOXBs8&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=7