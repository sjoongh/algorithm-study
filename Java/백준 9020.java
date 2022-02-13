import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		// 골드바흐 추측
		// 1보다 큰 자연수 중에서 1과 자기 자신을 제외한 약수가 없는 자연수 : 소수
		// 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다
		// 짝수n을 만드는 것 중 두 소수의 차이가 가장 작은 것을 출력!
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		
		for (int i = 0; i < t; i++) {
			int n = sc.nextInt();
			
            // 두 수의 차이가 가장 작은 것을 출력해야 하므로 n의 절반값부터 검사
			int up, down; // 16
			up = n / 2; // 8
			down = n - up; // 8
			
			while (true) {
                // 두 수 모두 소수여야 하므로 판별
				if (checking(up) && checking(down)) {
					break;  
                    // 소수가 아니라면 소수인 수를 찾기위해 up && down
				} else {
					up--; // 처음 나눈 반이 소수가 아니라면 하나는 낮추고 하나는 높임
					down++;
				}
			}
			System.out.println(up + " " + down);
		}
		}
	static boolean checking(int n) {
		boolean check = true;
        // n이 2이상 <= n의제곱근에서 나누어 떨어지면 소수가 아니다.
        // 1과 자기자신만 존재해야 소수이므로
		for (int i = 2; i <= Math.sqrt(n); i++) { // Math.sqrt(n) : n의 제곱근을 구함
			if (n % i == 0)
				check = false; // 소수면 true 리턴
		}
		return check;
	}
	}

