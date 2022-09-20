/**
 * Quiz3
 */
public class Quiz3 {
    public static void main(String[] args) {
        int num1 = 6;
        int num2 = 10;
        num1 = num2;
        num2 = num1;
        System.out.println(num1 + ", " + num2);

        int num3 = 6;
        int num4 = 10;
        num3 = num3 + num4;
        num4 = num3 + num4;
        System.out.println(num3 + ", " + num4);
    }
}