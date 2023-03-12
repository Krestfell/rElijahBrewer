import java.util.Scanner;

public class textLengthDemo {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter Text");
        String txt = in.nextLine();

        for (int i = 0; i < txt.length(); i++) {
            System.out.println(txt.charAt(i));
        }

        System.out.println("-----Reverse Text-----");
        for (int i = txt.length(); -1; )
    }
}

//! UNFINISHED
