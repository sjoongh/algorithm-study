package day15_network;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuffer sb;
		
		int n = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < n; i++) {
			sb = new StringBuffer();
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			while(st.hasMoreTokens()) {
				String next = st.nextToken();
				for (int j = next.length() -1; j >= 0; j--) {
					sb.append(next.charAt(j));
				}
				sb.append(" ");
			}
			bw.write(sb.toString()+"\n");
		}
		bw.flush();
		bw.close();
	}
}
