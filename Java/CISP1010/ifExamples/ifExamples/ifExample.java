package ifExamples;
import java.util.Scanner;

public class ifExample {

    public static void main(String[] args) {
        int actualFloor;
        Scanner in = new Scanner(System.in);
        System.out.println("Enter floor number ");
        int floor = in.nextInt();
        if (floor  > 13) {
          actualFloor = --floor;
        }
        else{

        }
        System.out.println(floor);
    }
}