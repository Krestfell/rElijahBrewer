package broArrays;

// 2D array: an array of arrays

public class Arrays2DBro {
    public static void main(String[] args) {

        String[][] cars = new String[3][3];
        // Think of this like a 3/3 block (3 rows, 3 columns)
        cars[0][0] = "Mustang";
        cars[0][1] = "Tesla";
        cars[0][2] = "FJ Cruiser";
        cars[1][0] = "Lancia";
        cars[1][1] = "Thunderbird";
        cars[1][2] = "Corvette";
        cars[2][0] = "Impala";
        cars[2][1] = "Ferrari";
        cars[2][2] = "Firebird";

        /*
         * .
         * Can also be added like so:
         * String[][] cars = {
         * 
         * {"Mustang","Tesla","FJ Cruiser"},
         * 
         * {"Lancia","Thunderbird","Corvette"},
         * 
         * {"Impala","Ferrari","Firebird"}
         * 
         * };
         * 
         */

        // Display in a nested for loop
        for (int i = 0; i < cars.length; i++) {
            System.out.println();
            for (int j = 0; j < cars[i].length; j++) {
                System.out.println(cars[i][j] + " ");
            }
        }
    }
}

// * Java 2D arrays
// https://www.youtube.com/watch?v=alwukGslBG8&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=16