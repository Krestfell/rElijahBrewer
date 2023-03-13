package broLoops;

import java.util.ArrayList;

//  for-each = 	traversing technique to iterate through the elements in an  array/collection
//	less steps, more readable
//	less flexible

public class forEachLoopBro {
    public static void main(String[] args) {

        // String[] animals = { "cat", "dog", "rat", "bird" };

        ArrayList<String> animals = new ArrayList();

        animals.add("cat");
        animals.add("dog");
        animals.add("rat");
        animals.add("bird");

        for (String i : animals) {
            System.out.println(i);
        }
    }
}

// * java for-each loop
// https://www.youtube.com/watch?v=_IT8F5W0ZO4&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=21