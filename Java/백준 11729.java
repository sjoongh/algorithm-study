import java.util.*;

public class Main {
	static StringBuffer sb = new StringBuffer();
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		System.out.println((int)Math.pow(2, num)-1);
		hanoi(1,2,3,num);
		System.out.println(sb.toString());
	}
	
	public static void hanoi(int x, int y, int z, int n) {
		if(n == 0) return;
		else {
			// 1~(N-1)번째 원판을 X장대에서 Y장대로 옮기기
			hanoi(x,z,y,n-1);
			// N번째 원판을 X장대에서 Z장대로 옮기기
			sb.append(x + " " + z + "\n");
			// 1~(N-1)번째 원판을 Y장대에서 Z장대로 옮기기
			hanoi(y,x,z,n-1);
		}
	}
}