package WhileLoopDemo;

public class WhileLoopPractice {

    public static void main(String[] args) {

        int n = 100;
        int i = 0;

        while (i * i < n) {
            System.out.println(i * i);
            i = i + 1;
        }

        System.out.println("------------------------------------------------");
        int j = 1;
        while (j < n) {
            if (j % 10 == 0) {
                System.out.println(j);
            }
            j++;
        }
    }
}
