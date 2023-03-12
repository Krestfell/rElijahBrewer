package src;

import java.util.ArrayList;

public class sequence {
    private ArrayList<Integer> values;

    public sequence() {
        values = new ArrayList<>();
    }

    public void add(int n) {
        values.add(n);
    }

    public String toString() {
        return values.toString();
    }

    public sequence append(sequence other) {
        sequence result = new sequence();

        for (int i = 0; i < other.values.size(); i++) {
            int j = other.values.get(i);
            result.add(j);
        }
        return result;
    }
}