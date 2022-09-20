public class countertester {
     public static void main(String[] args) {
        Counter counter = new Counter();
        System.out.println(counter.display());
        counter.increment();
        counter.increment();
        counter.increment();
        System.out.println(counter.display());
        counter.reset();
        System.out.println(counter.display());
        Counter counter2 = new Counter(10);
        counter2.increment();
        counter2.increment();
        counter2.increment();
        counter2.increment();
        counter2.increment();
        System.out.println(counter2.display());
        Counter counter3 = new Counter(10);
        counter3.increment(10);
        System.out.println(counter3.display());
    }
}
