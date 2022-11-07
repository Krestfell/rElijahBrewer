package broArrays;

// Array: Used to store multiple values in a single variable.

public class ArraysBro {
    public static void main(String[] args) {
        // Method 1

        String[] cars = { "Mustang", "Tesla", "FJ Cruiser" };
        // The names inside curlys are called elements

        // In order to access an element:
        cars[0] = "Lancia";

        // Display
        System.out.println(cars[0]);
        System.out.println();

        // ----------------------------------------------------------------

        // Method 2
        String[] cars2 = new String[3];
        // Set number of elements and the assign them values
        cars2[0] = "Mustang";
        cars2[1] = "Tesla";
        cars2[2] = "FJ Cruiser";

        // Display all in a for loop
        for (int i = 0; i < cars2.length; i++) {
            System.out.println(cars2[i]);
        }
    }
}

// * Java arrays
// https://www.youtube.com/watch?v=ei_4Nt7XWOw&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=15