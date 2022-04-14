import java.io.*;

public class Main {

    static int max=0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int t[] = new int[n+10];
        int p[] = new int[n+10];
        int dp[] = new int[n+10];

        String tmp[];

        for (int i = 1; i <= n; i++) {
            tmp = br.readLine().split(" ");
            t[i] = Integer.parseInt(tmp[0]);
            p[i] = Integer.parseInt(tmp[1]);
        }


        for (int i=n;i>0;i--) {
            int next = i+ t[i];
            if (next > n+1 ) {
                dp[i] = dp[i+1];
            }
            else {
                dp[i] = Math.max(dp[i+1],dp[next]+p[i]);
            }
        }
        System.out.println(dp[1]);
    }
}