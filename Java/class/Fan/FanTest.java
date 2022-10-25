public class FanTest {

    public static void main(String[] args) {
        Fan Fan1 = new Fan();
        Fan1.setSpeed(Fan.MED);
        Fan1.setFanOn(false);
        Fan1.setLightOn(true);
 
        System.out.println(Fan1.toString());
     }

}