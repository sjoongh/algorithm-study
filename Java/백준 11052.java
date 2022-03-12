import java.util.*;

public class Main {
    public static void Main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] arr = new int[n+1]; // 1부터 돌아가므로 +1
        int[] result = new int[n+1];

        for (int i = 1; i <= n; i++) {
            arr[i] = sc.nextInt();
        }
        // dp 구현시에는 일반항 상태로 정의하는 것이 중요하다
        // 카드 i개를 구매하는 방법은?
        // 카드 1개가 들어있는 카드팩을 구매하고, 카드 i-1개를 구입한다.
        // 카드 2개가 들어있는 카드팩을 구매하고, 카드 i-2개를 구입한다.
        // 카드 3개가 들어있는 카드팩을 구매하고, 카드 i-3개를 구입한다.
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) { // i의 크기만큼 돌아가도록
                // result의 현재값에는 arr의 최대 값이 출력
                result[i] = Math.max(result[i], result[i - j] + arr[j]);
            }
        }
        System.out.println(result[n]);
    }
}