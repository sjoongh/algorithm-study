import java.util.Scanner;

public class 백준 9020 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int test = 0;
        for (int i = 0; i < t; i++) {
            test = sc.nextInt();
            if (i == test) {
                test = t;
            }
        }
    }
}
