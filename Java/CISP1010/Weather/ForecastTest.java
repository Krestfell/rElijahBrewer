
public class ForecastTest {
    public static void main(String[] args) {
        Forecast wf1 = new Forecast(70, "sunny");

        System.out.print("The temperature is " + wf1.getTemperature());
        System.out.println("F or " + wf1.fahrenheitToCelsius() + "C");
        System.out.println("The sky condition  is " + wf1.getSky());
    }
}
