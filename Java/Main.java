import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] A = new int[n];
        for (int i = 0; i < n; i++) {
            A[i] = sc.nextInt();
        }
        Arrays.sort(A);
        int m = sc.nextInt();
        int left = 0;
        int right = A.length - 1;
        boolean find = false;
        for (int i = 0; i < m; i++) {
            int num = sc.nextInt();
            while (left <= right) {
                int midIndex = (left + right) / 2;
                int midValue = A[midIndex];
                if (midValue > num) {
                    right = midIndex - 1;
                } else if (midValue < num) {
                    left = midIndex + 1;
                } else { //찾음
                    find = true;
                    System.out.println(1);
                    break;
                }
            }
            if (!find) {
                System.out.println(0);
            }
        }
    }
}