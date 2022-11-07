public class CylinderCW {

    double pi = Math.PI;
    private double radius;
    private double height;
    private double area = radius*radius*pi;
    private double vol = area*height;

    public CylinderCW() {
    }

    public CylinderCW(double radius, double height) {
        this.radius = radius;
        this.height = height;
    }

    public double getRadius() {
        return radius;
    }

    public double getHeight() {
        return height;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public double calculateArea() {
        return area;
    }

    public double calculateVolume() {
        return vol;
    }
}