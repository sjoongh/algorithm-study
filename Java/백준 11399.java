import java.util.*;

public class Main {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int result = 0;
        int add = 0;
        int[] s = new int[n];
        for (int i = 0; i < n; i++) {
            s[i] = sc.nextInt();
        }
        Arrays.sort(s);
        for (int i = 0; i < n; i++) {
                add += s[i];
                result += add;
        }
        System.out.println(result);
    }
}