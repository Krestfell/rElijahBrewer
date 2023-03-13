package broArrays;

import java.util.ArrayList;

public class ArrayLists2DBro {
    public static void main(String[] args) {

        ArrayList<ArrayList<String>> groceryList = new ArrayList();

        ArrayList<String> bakeryList = new ArrayList();
        bakeryList.add("pasta");
        bakeryList.add("bread");
        bakeryList.add("donuts");

        ArrayList<String> produceList = new ArrayList();
        produceList.add("tomatoes");
        produceList.add("onions");
        produceList.add("peppers");
        produceList.add("apples");

        ArrayList<String> drinksList = new ArrayList();
        drinksList.add("soda");
        drinksList.add("coffee");

        groceryList.add(bakeryList);
        groceryList.add(produceList);
        groceryList.add(drinksList);

        System.out.println(groceryList.get(1).get(2));
    }
}

// * Java 2D ArrayList
// https://www.youtube.com/watch?v=9tBxJoQF74E&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=20