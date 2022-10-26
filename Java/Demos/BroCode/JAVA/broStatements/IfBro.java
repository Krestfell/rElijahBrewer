package broStatements;
public class IfBro {

    public static void main(String[] args) {

        int age = 66;

        // If statements preform a block of code if it's condition is true.
        if (age == 100) {
            System.out.println("Congrats on a century!");
        } else if (age >= 65) {
            System.out.println("OK Boomer");
        } else if (age >= 18) {
            System.out.println("You are an adult");
        } else if (age >= 13) {
            System.out.println("OK Zoomer");
        } else {
            System.out.println("You are not an adult");
        }
    }
}

// * Java if statements
// https://www.youtube.com/watch?v=MY03bt_0JQI&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=9