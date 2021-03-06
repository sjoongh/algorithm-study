import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int arr[] = new int[n + 1];
        int dp[] = new int[n + 1];

        for (int i = 1; i <= n; i++)
            arr[i] = sc.nextInt();

        dp[1] = 1;

        for (int i = 2; i <= n; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (arr[i] < arr[j] && dp[i] <= dp[j]) {
                    dp[i] = dp[j] + 1;
                } else if (arr[i] == arr[j]) {
                    dp[i] = dp[j];
                }
            }
        }
        int result = 0;

        for (int i = 1; i <= n; i++)
            result = Math.max(dp[i], result);
        System.out.println(result);
    }
}​