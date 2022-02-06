import java.util.*;
import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a, b;
        int[] c = new int[100];
        int result = 0;

        a = sc.nextInt();
        b = sc.nextInt();
        for (int i = 0; i < a; i++) {
            c[i] = sc.nextInt();
        }

        for (int i = 0; i < a-2; i++) {
            for (int j = i+1; j < a-1; j++) {
                for (int k = j+1; k < a; k++) {
                    if (c[i]+c[j]+c[k] > b) {
                        continue;
                    } else {
                        result = Math.max(result, c[i]+c[j]+c[k]);
                    }
                }
            }
        }
        System.out.println(result);
        
    }
    
}
