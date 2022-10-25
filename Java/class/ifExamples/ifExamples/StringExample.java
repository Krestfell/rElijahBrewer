package ifExamples;

import java.util.Scanner;

public class StringExample {
    public static void main(String[] args) {
        String txt1 = "Chatt";
        System.out.println("Enter name ");
        Scanner in = new Scanner(System.in);
        String txt2 = in.next();
        if (txt1.equals(txt2)) {
            System.out.println("txt1 = txt2");
        }
        else {
            System.out.println("txt1 does not match txt2");
        }
    }
}
