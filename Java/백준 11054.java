import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int n = in.nextInt();
		int a[] = new int[n];
		int l_dp[] = new int[n];
		int r_dp[] = new int[n];
		
		for(int i=0;i<n;i++) {
			a[i] = in.nextInt();
		}
		
		// LIS
		for(int i=0;i<n;i++) {
			l_dp[i] = 1;
			
			for(int j=0;j<i;j++) {
				if(a[j]<a[i] && l_dp[i] < l_dp[j]+1) {
					l_dp[i] = l_dp[j]+1;
				}
			}
		}
		
		// LDS
		for(int i=n-1;i>=0;i--) {
			r_dp[i] = 1;
			
			for(int j=n-1;j>i;j--) {
				if(a[j]<a[i] && r_dp[i] < r_dp[j]+1) {
					r_dp[i] = r_dp[j]+1;
				}
			}
		}
		
		int max = Integer.MIN_VALUE;
		
        // LIS와 LDS의 부분수열 길이의 합 중 최댓값을 찾는다.
		for(int i=0;i<n;i++) {
			if(max<l_dp[i]+r_dp[i]) {
				max = l_dp[i] + r_dp[i];
			}
		}
		
        // 중복 제거를 위한 -1
		System.out.println(max - 1);
		
		in.close();
	}

}
