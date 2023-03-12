/**
 * Write a class for the weather forecast, assuming that it has the following
 * attributes:
 * The temperature in Fahrenheit; the default value is 70.
 * The sky conditions, which could be sunny, snowy, cloudy, or rainy; the
 * default value is sunny.
 * Include default constructor, overloaded constructor, the accessors, and the
 * mutators
 * Include a method that convert Fahrenheit to Celsius.
 * Celsius Temperature = (Fahrenheit temperature – 32) * 5 / 9.
 * Write a tester class to test all the method in your class.
 */
public class Forecast {
    private double temperature; // in Fahrenheit
    private String sky;

    // sets temperature to 70.0 and sky to sunny
    public Forecast() {
        temperature = 70;
        sky = "sunny";
    }

    public Forecast(double newTemperature, String newSky) {
        temperature = newTemperature;
        sky = newSky;
    }

    // getTemperature method
    public double getTemperature() {
        return temperature;
    }

    // getSky method
    public String getSky() {
        return sky;
    }

    // fahrenheitToCelsius method
    public double fahrenheitToCelsius() {
        temperature = temperature - 32;
        temperature = temperature * 5;
        temperature = temperature / 9;
        return temperature;
    }
}