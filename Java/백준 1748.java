import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws  Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String num = br.readLine();
        int result = 0;
        int x = 9;
        int y = 0;
        
        for(int i = 1 ; i < num.length(); i++){
        	if (num.length() == 1) {
        		result = Integer.parseInt(num);
        	} else {
        		y += x * i;
        		x *= 10;
        	}
        }
        double z = Math.pow(10, num.length()-1); // 10의 제곱승
        // 1의 자리 더하기 + 2의 자리 더하기 + (입력받은 값 - 10의 제곱승(배열의 자릿수-1) * 배열의자릿수) + 배열의 자리수 
        int test = Integer.parseInt(num);
        test -= z;
        result += y + (test * num.length()) + num.length();
        
        System.out.println(result);
    }
}