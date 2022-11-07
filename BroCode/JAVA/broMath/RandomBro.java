package broMath;

import java.util.Random;

public class RandomBro {

    public static void main(String[] args) {

        Random random = new Random();
        // The Random class is used to generate a stream of pseudorandom numbers.

        int n = random.nextInt() + 1;
        // Generates a random number between the set bounds.

        double r = random.nextDouble();
        // Generates a random number between 0-1.

        boolean z = random.nextBoolean();
        // Randomly generates true or false.

        System.out.println(n);
        System.out.println(r);
        System.out.println(z);
    }
}

// * Java random numbers
// https://www.youtube.com/watch?v=VMZLPl16P5c&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=8