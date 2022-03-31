import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
 
public class Main {
	
    private static int n;
    private static int[] arr;
    private static int[] result;
    static boolean[] visit;
    
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	n = Integer.parseInt(br.readLine());
    	arr = new int[n];
    	result = new int[n];
    	visit = new boolean[n]; // 초기값 false임

    	for (int i=0; i < n; i++) {
    		arr[i] = i;
    	}
    	print(0);
    }
    public static void print(int depth) {
        if(depth == n) {
            for(int i = 0; i < n; i++) {
                System.out.print(result[i]+1+ " ");
            }
            System.out.println();
        } else {
        	System.out.println("재귀 시작점");
        for(int i = 0; i < n; i++) {
        	System.out.println(i+" for문 동작");
            if(!visit[i]) {
                visit[i] = true;
                result[depth] = arr[i];
                print(depth+1);
                visit[i] = false;
                System.out.println("재귀 빠져나옴");
            }
            System.out.println("재귀 for문 끝단");
        }
        }
    } 
}