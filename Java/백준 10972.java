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
        
        for(int i = 0; i < n; i++) {
        	arr[i] = Integer.parseInt(st.nextToken());
        }
        if (next(arr)) {
            for (int i=0; i<n; i++) {
                System.out.print(arr[i] + " ");
            }
        } 
        else {
            System.out.println("-1");
        }
    }
    
    private static boolean next(int[] arr) {
        //    	ex) 7 1 2 3 6 5 4 1
//    1. 오른쪽부터 왼쪽이 작은 수를 찾는다. 3 < 6, 6선택 i = 3
//    2. 다시 오른쪽부터 확인해서 3보다 첫번째로 큰 숫자를 찾는다. -> 4
//    3. 3과 4를 자리를 바꾼다 -> 7 2 4 6 5 3 1
//    4. 바꾼 숫자의 오른쪽 전부를 뒤집는다. -> 7 2 4 1 3 5 6
        int i = arr.length-1;
        // i는 오른쪽부터 돌아감
        // arr[i-1] : 현재 i값보다 한칸 왼쪽에 있는 값
        // arr[i] : 현재 i 값
        // i의 왼쪽에 있는값이 오른쪽에 있는 값보다 클 경우 i--;
        // 즉 arr[i-1] < arr[i]가 되는 값을 찾음, 즉 왼쪽의 값이 오른쪽값보다 작은 첫번째 값을 찾음
        while (i > 0 && arr[i-1] >= arr[i]) i--;
        // 처음부터 내림차순 정렬일 경우 위의 while문이 돌아갈때 i--로 인해 0이 되므로 -1 출력
        if (i <= 0) return false;

        int j = arr.length-1;
        // 다시 오른쪽부터 돌아가 i에서 찾은 수 보다 큰 수를 찾음
        // arr[i-1] >= arr[j]일 경우에만 j--이므로 arr[i-1]보다 작은 배열의 값에 해당할때만 j--;
        // --> 결과적으로 오른쪽에서 가장 큰 수를 찾아냄
        while (arr[i-1] >= arr[j]) j--;
        // 찾은 결과 swap
        swap(arr, i-1, j);

        j = arr.length-1;
        // 비교 한 이후의 오른쪽 숫자를 i부터 전부 오름차순 정렬
        if (i < j) {
            swap(arr, i, j);
            i++;
            j--;
        }
    }

    private static void swap(int[] arr, int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
}