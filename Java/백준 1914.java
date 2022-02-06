import java.util.*;

public class Main {
    // StringBuffer는 단 한번 생성됨
   static StringBuffer sb = new StringBuffer();
   
   public static void main(String[] args) {
      
      Scanner sc = new Scanner(System.in);
      int num = sc.nextInt();
      System.out.println((int)Math.pow(2, num)-1);
      hanoi(1,2,3,num);
      System.out.println(sb.toString()); // 전체 과정 출력
   }
   
   public static void hanoi(int x, int y, int z, int n) {
      if(n == 0) return; // hanoi 종료
      else { // n개의 원판이 옮겨질때까지 자리 변경
         hanoi(x,z,y,n-1);
         sb.append(x + " " + z + "\n"); // append 마다 새로운 string객체
         hanoi(y,x,z,n-1);
      }
   }
}