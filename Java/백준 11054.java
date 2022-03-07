import java.util.Scanner;
import javafx.scene.chart.ScatterChart;
public class Main {
    	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int a[] = new int[n];
		int l_dp[] = new int[n];
		int r_dp[] = new int[n];
		
		for(int i=0;i<n;i++) { a[i] = sc.nextInt(); }
		
		for(int i=0;i<n;i++) {
			l_dp[i] = 1;
			
			for(int j=0;j<i;j++) {
				if(a[j]<a[i] && l_dp[i] < l_dp[j]+1) {
					l_dp[i] = l_dp[j]+1;
				}
			}
		}
		for(int i=n-1;i>=0;i--) {
			r_dp[i] = 1;
			
			for(int j=n-1;j>i;j--) {
				if(a[j]<a[i] && r_dp[i] < r_dp[j]+1) {
					r_dp[i] = r_dp[j]+1;
				}
			}
		}
		int max = Integer.MIN_VALUE;
		for(int i=0;i<n;i++) {
			if(max<l_dp[i]+r_dp[i]) {
				max = l_dp[i] + r_dp[i];
			}
		}
		System.out.println(max - 1);
	}

}
