
/**
 * nestedFiles
 */
import java.util.Scanner;

public class nested2 {

    public static void main(String[] args) {
        int score;
        String grade;
        Scanner in = new Scanner(System.in);
        System.out.println("Enter score");
        score = in.nextInt();
        if (score < 60) {
            grade = "F";
        } else if (score < 70) {
            grade = "D";
        } else if (score < 80) {
            grade = "C";
        } else if (score < 90) {
            grade = "B";
        } else {
            grade = "A";
        }
        System.out.println("Grade: " + grade);
    }
}