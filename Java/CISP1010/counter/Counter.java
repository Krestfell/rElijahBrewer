/**
 * Counter class - Tally counter emulator.
 * @author Krestfell
 */

public class Counter {
    private int number;
    public Counter (){   
    }
    public Counter (int number) {
        this.number = number;
    }
    public void increment (){
        number = number + 1;
    }
    public void increment(int amount){
        this.number = this.number + amount;
    }
    public void decrement(){
        number = number -1;
    }
    public void reset() {
        number = 0;
    }
    public int display() {
        return number;
    }
} 