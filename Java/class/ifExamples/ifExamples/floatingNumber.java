package ifExamples;

public class floatingNumber {
    public static void main(String[] args) {
        double r = Math.sqrt(2);
        double d = r * r - 2;
        if (d < Math.E) {
            System.out.println("r * r - 2 = 0");
        }
        else{
            System.out.println("r * r - 2 = " + d);
            
        }
    }
}
