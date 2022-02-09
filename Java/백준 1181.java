import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
	
	public static void main(String args[]) {
            Scanner sc = new Scanner(System.in);
        
	   	 	int num = sc.nextInt();
	   	 	
	   	 	String[] arr = new String[num];
	   	 	
	   	 	for(int i =  0 ; i < num ; i++) {
	   	 		arr[i] = sc.next();
	   	 	}
	   	 	// Comparator : 인터페이스, 기본정렬이 아닌 다른 기준으로 사용할 때
	   	 	Arrays.sort(arr, new Comparator<String>() {
	   	 		@Override
	   	 		public int compare(String s1, String s2) {
	   	 		if(s1.length() == s2.length()) {// 길이가 같다면
                    // compareTo : s1과 s2를 비교(아스키코드값 기반 && 같은 위치의 문자만 비교)
	   	 			return s1.compareTo(s2);
	   	 		}else {// 길이가 다르다면 길이만큼 빼줌
	   	 			return s1.length() - s2.length();
	   	 		}
	   	 		
	   	 	}
	   	 	});
	   
	   	 	System.out.println(arr[0]);
	   	 	for(int i = 1; i < num; i++) {
                     // 앞&뒤 비교시 중복되지 않는 단어만 출력
	   		if (!arr[i].equals(arr[i - 1])) {
				System.out.println(arr[i]);
			}
		}
	}
}