public class SwitchBro {

    // Switch allows a variable to be tested for equality against a list of values.
    // Switches can have multiple possible execution paths.
    //
    // The switch can be used in two ways:
    //
    // 1) Using the switch() method:
    //
    // switch (switchVar) {
    // case 0:

    public static void main(String[] args) {

        String day = "bro";

        switch (day) {
            case "Sunday":
                System.out.println("It is Sunday");
                break;
            case "Monday":
                System.out.println("It is Monday");
                break;
            case "Tuesday":
                System.out.println("It is Tuesday");
                break;
            case "Wednesday":
                System.out.println("It is Wednesday");
                break;
            case "Thursday":
                System.out.println("It is Thursday");
                break;
            case "Friday":
                System.out.println("It is Friday");
                break;
            case "Saturday":
                System.out.println("It is Saturday");
                break;
            // It's important to add break to continue the code normally.
            default:
                System.out.println(day + " is invalid");
                // If an invalid input is given, this will be the output.
        }
    }
}

// * Java switch
// https://www.youtube.com/watch?v=Om3qzMoaIUo&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=10