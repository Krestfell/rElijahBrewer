package broMain;

// String: a reference data type that can store one or more characters
// Reference data types have access to useful methods

public class StringMethodsBro {
    public static void main(String[] args) {
        String name = "Bro";

        // boolean result = name.equalsIgnoreCase("bro");
        // int result = name.length();
        // char result = name.charAt(0);
        // int result = name.indexOf("o");
        // boolean result = name.isEmpty();
        // String result = name.toUpperCase();
        // String result = name.toLowerCase();
        // String result = name.trim();
        String result = name.replace('o', 'a');

        System.out.println(result);
    }
}

// *Java String Methods
// https://www.youtube.com/watch?v=P9hEmbfdiuc&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=17