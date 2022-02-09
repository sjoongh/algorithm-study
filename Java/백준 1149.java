import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringTokenizer st; // ("문자열", "구분자")로 사용
		int n = Integer.parseInt(sc.nextLine());
		
		int[][] color = new int[n][3];
		
		for (int i = 0; i < n; i++) { // 입력값 
			// 입력값+공백
			st = new StringTokenizer(sc.nextLine(), " ");
			color[i][0] = Integer.parseInt(st.nextToken()); // 다음 토큰을 반환함
			color[i][1] = Integer.parseInt(st.nextToken());
			color[i][2] = Integer.parseInt(st.nextToken());
		}
		
		for (int i = 1; i < n; i++) { // i-1로 전값과 비교해서 최소값을 출력하므로 i = 1부터 시작해야함
			color[i][0] = color[i][0] + Math.min(color[i-1][1], color[i-1][2]);
		    color[i][1] = color[i][1] + Math.min(color[i-1][0], color[i-1][2]);
		    color[i][2] = color[i][2] + Math.min(color[i-1][0], color[i-1][1]);
		}
		System.out.println(Math.min(Math.min(color[n - 1][0], color[n - 1][1]), color[n - 1][2])); // 세가지 색깔의 마지막값 중 가장 작은 값 출력
	}

}
