import java.util.*;

public class Main {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int y = sc.nextInt();
        sc.close();

        if (y < 45) {
            x--;
            y = 60 - (45 - y);

            if (x < 0) {
                x = 23;
            }
            System.out.println(x + " " + y);
        } else {
            System.out.println(x + " " + (y-45));
        }
    }
}