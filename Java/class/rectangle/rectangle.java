package rectangle;
import java.awt.Rectangle;
public class rectangle {

    public static void main(String[] args) {

        Rectangle box = new Rectangle();
        System.out.println(box);
        Rectangle box1 = new Rectangle(10,20,30,40);
         System.out.println(box1);
         System.out.println("x = " + box1.getX());
         System.out.println("Width = " + box1.getWidth());
         box1.translate(10,10);
         System.out.println(box1);

         System.out.println("-Object References-");
         Rectangle box2 = new Rectangle(11,22,44,66);
         Rectangle box3 = box2;
         System.out.println(box2);
         System.out.println(box3);
         box3.translate(100,100);
         System.out.println("-After translate-");
         System.out.println(box2);
         System.out.println(box3);
    }
}