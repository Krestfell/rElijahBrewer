
public class Circle {

    private double radius = 15;

    public Circle() {

    }

    public Circle(double radius) {
        this.radius = radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    public double getArea() {
        return 3.14 * radius * radius;
    }
}
