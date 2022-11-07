package Source;

import java.util.Arrays;

public class TrueCopy {
    public static void main(String[] args) {
        double[] val = {3.5, 77, 66.9, 23, 8, 123};
        double[] val2 = val;
        double[] val3 = Arrays.copyOf(val, val.length);
        for (int i = 0; i < val.length; i++) {
    }
}
