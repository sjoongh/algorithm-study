import java.util.Scanner;
import java.util.Stack;
import java.util.StringTokenizer;
import java.io.*;

public class Main {
   public static void main(String[] args) throws IOException {
      Stack<Integer> stack = new Stack<Integer>();
      StringTokenizer stringTokenizer;
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	  Scanner sc = new Scanner(System.in);
    
      int cnt = Integer.parseInt(br.readLine());
  
      for(int i = 0; i < cnt; i++) {
          stringTokenizer = new StringTokenizer(br.readLine()); 
    	  String input = stringTokenizer.nextToken(); // push시 숫자 공백을 구분하기 위해 사용
    	  if(input.contains("push")) {
    		int input2 = Integer.parseInt(stringTokenizer.nextToken()); // 숫자 걸러냄
    		stack.push(input2); // stack에 숫자만 push
    	  }else if(input.equals("pop")){
    		System.out.println(stack.isEmpty() ? -1 : stack.pop());
    	  }else if(input.equals("size")) {
    		System.out.println(stack.size());
    	  }else if(input.equals("empty")) {
    		System.out.println(stack.isEmpty() ? 1 : 0);
    	  }else if(input.equals("top")) {
    		System.out.println(stack.isEmpty() ? -1 : stack.peek());
    	  }
      }
   }
}