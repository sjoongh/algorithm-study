import java.util.*;

public class Main {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();
        int x = sc.nextInt();

        for (int i = 0; i < num; i++) {
            int number = sc.nextInt();
            if (number < x) {
                System.out.print(number+" ");
            }
        }
    }
}