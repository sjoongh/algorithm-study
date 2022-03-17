package programmers;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int[] arr;
	static boolean[] result;
	
    public static void main(String[] args) throws Exception {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	while (true) {
    		StringTokenizer st = new StringTokenizer(br.readLine());
    		n = Integer.parseInt(st.nextToken());
    		if (n == 0) {
    			break;
    		}
    	
    	arr = new int[n];
    	result = new boolean[n];
    	for (int i = 0; i < n; i++) {
    		arr[i] = Integer.parseInt(st.nextToken());
    	}
    	
    	dfs(0, 0);
    	System.out.println();
    	}
    }
    private static void dfs(int start, int d) {
    	if (d == 6) {
    		for (int i = 0; i < n; i++) {
    			if (result[i]) {
    				System.out.print(arr[i] + " ");
    			}
    		}
    		System.out.println();
    	}
    	for (int i = start; i < n; i++) {
    		result[i] = true;
    		dfs(i+1, d+1);
    		result[i] = false;
    	}
    }
}