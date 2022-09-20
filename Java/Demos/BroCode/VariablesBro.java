public class VariablesBro {

    public static void main(String[] args) {

        // * Variables are containers for storing data values.
        // There are 2 data types called primitive and reference. Here's the difference:

        /**
         * Primitive Data Type:
         * 
         * 8 types (boolean, byte, int, etc).
         * Stores data.
         * Can only hold 1 value.
         * Less memory.
         * Fast.
         */

        /**
         * Reference Data Type:
         * 
         * Unlimited types (user defined).
         * Stores an address.
         * Can hold more than 1 value.
         * More memory.
         * Slower.
         */

        // __________________________________________________

        // * declaration + assignment = initialization:

        int z; // declaration
        z = 21; // assignment
        int Z = 21; // initialization
        String name = "Elijah";

        System.out.println("Hello," + name + "! You are " + Z + " years old.");

        // __________________________________________________

        // Variable examples:

        boolean q = true;
        // * ^ Primitive. Size: 1 bit. Value: true/false.

        double u = 6.0;
        // * ^ Primitive. Size: 8 bytes. Value: fractional # up to 15 digits.

        char pushin = 'P';
        // * ^ Primitive. Size: 2 bytes. Value: single character/letter/ASCII.

        String word = "Bro";
        // * ^ Reference. Size: varies. Value: A sequence of characters.

        int r = 3;
        // * ^ Primitive. Size: 4 bytes. Value: -2 billion to 2 billion

        byte w = 1;
        // ^ Primitive. Size: 1 byte. Value: -128 to 127.

        short e = 2;
        // ^ Primitive. Size: 2 bytes. Value: -32,768 to 32,767

        long t = 4L;
        // ^ Primitive. Size: 8 Bytes. Value: -9 quintillion to 9 quintillion.

        float i = 5.0f;
        // ^ Primitive. Size: 8 bytes. Value: fractional # up to 6-7 digits.

        // __________________________________________________

        // * Swap two variables:

        String x = "Water";
        String y = "Kool-Aid";
        String temp;

        temp = x;
        x = y;
        y = temp;

        System.out.println("x: " + x + "\ny: " + y);
    }

}

// * Variables in Java
// https://www.youtube.com/watch?v=so1iUWaLmKA&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=2

// * Swap 2 variables in Java
// https://www.youtube.com/watch?v=G0mFJUFMzjs&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=3

