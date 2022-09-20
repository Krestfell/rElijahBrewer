
import java.util.Scanner;

/**
 * ScannerDemo
 */
 public class ScannerDemo {
public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    System.out.println("Enter name ");
    String name = in.nextLine();
    System.out.println(name);
    System.out.println("Enter age ");
    int age = in.nextInt();
    System.out.println(age);
    }
 }