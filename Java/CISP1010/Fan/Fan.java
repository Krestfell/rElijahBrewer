// Create a Fan class that emulates the fan control switch

public class Fan {
    public static final char LOW = 'L';
    public static final char MED = 'M';
    public static final char HI = 'H';

    private char speed;
    private boolean fanOn;
    private boolean lightOn;

    public Fan() {

    }

    public Fan(char speed, boolean fanOn, boolean lightOn) {

    }

    public void setSpeed(char speed) {
        this.speed = speed;
    }

    public void setFanOn(boolean fanOn) {
        this.fanOn = fanOn;
    }

    public void setLightOn(boolean lightOn) {
        this.lightOn = lightOn;
    }

    public char getSpeed() {
        return speed;

    }

    public boolean isFanOn() {
        return fanOn;

    }

    public boolean isLightOn() {
        return lightOn;

    }
    
    public String toString(){
        return "Fan (" + "Speed= " + speed +", fanOn= " + fanOn + ", lightOn= " + lightOn + ")";
    }
}