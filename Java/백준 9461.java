import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
 
public class Main {
	static long[] test = new long[101];
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		pado();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < T; i++) {
			sb.append(test[Integer.parseInt(br.readLine())]).append('\n');
		}
		
		System.out.println(sb);
	}
 
	public static void pado() {
		
		test[1] = 1;
		test[2] = 1;
		test[3] = 1;
 
		for (int i = 4; i < 101; i++) {
			test[i] = test[i - 2] + test[i - 3];
		}
	}
 
}