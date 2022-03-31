import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
 
public class Main {
	
	private static int a;
    
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int n = Integer.parseInt(br.readLine());
    	
    	StringBuilder sb = new StringBuilder();
    	for (int i = 0; i < n; i++) {
    		String[] input = br.readLine().split(" ");
    		
    		switch (input[0]) {
    		case "all":
    			a = (1 << 21) -1;
    			break;
    		case "empty":
    			a = 0;
    			break;
    		default:
    			int x = Integer.parseInt(input[1]);
    			switch (input[0]) {
                case "add":
                    a |= (1 << x);
                    break;
                case "remove":
                    a &= ~(1 << x);
                    break;
                case "check":
                    sb.append((a & (1 << x)) != 0 ? 1 : 0).append('\n');
                    break;
                case "toggle":
                    a ^= (1 << x);
                    break;
                    }
    			}
    		}
    	System.out.println(sb);
    	}
    }