package broArrays;

import java.util.ArrayList;

// ArrayList = 	a resizable array. 

//	Elements can be added and removed after compilation phase

//	store reference data types

public class ArrayListsBro {

    public static void main(String[] args) {

        ArrayList<String> food = new ArrayList<String>();

        food.add("pizza");
        food.add("burger");
        food.add("hotdog");

        food.set(0, "sushi");
        food.remove(2);
        food.clear();

        for (int i = 0; i < food.size(); i++) {
            System.out.println(food.get(i));
        }
    }
}

// * Java ArrayList
// https://www.youtube.com/watch?v=1nRj4ALuw7A&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=19