import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
 
public class Main {
 
    private static int n;
 
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	n = Integer.parseInt(br.readLine());
    	int arr[] = new int[n];
    	
    	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    	
    	for (int i = 0; i < n; i++) {
    		arr[i] = Integer.parseInt(st.nextToken());
    	}
    	
    	if (next(arr)) {
    		for (int i=0; i < n; i++) {
    			System.out.print(arr[i] + " ");
    		}
    	} else {
    		System.out.println("-1");
    	}
    }
    
    private static boolean next(int[] arr) {
    	int i = arr.length -1;
    	while (i > 0 && arr[i] > arr[i-1]) i--;
    	
    	if (i <= 0) return false;
    	
    	int j = arr.length -1;
    	while (arr[i-1] < arr[j]) j--;
    	
    	swap(arr, i-1, j);
    	j = arr.length - 1;
    	while (i < j) {
    		swap(arr, i, j);
    		i++;
    		j--;
    	}
    	return true;
    }
    
    private static void swap(int[] arr, int a, int b) {
    	int tmp = arr[a];
    	arr[a] = arr[b];
    	arr[b] = tmp;
    }
    
}