import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		// 골드바흐 추측
		// 1보다 큰 자연수 중에서 1과 자기 자신을 제외한 약수가 없는 자연수 : 소수
		// 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다
		// 짝수n을 만드는 것 중 두 소수의 차이가 가장 작은 것을 출력!
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for (int i = 0; i < T; i++) {
			int n = sc.nextInt();
			
            // 두 수의 차이가 가장 작은 것을 출력해야 하므로 n의 절반값부터 검사
			int div, rem;
			div = n / 2;
			rem = n - div;
			
			while (true) {
				if (isPrime(div) && isPrime(rem)) { // 두 수가 소수인지 판별
					break; // 소수라면 break로 while문 나감
				} else {
					div--; // 처음 나눈 반이 소수가 아니라면 하나는 낮추고 하나는 높임
					rem++;
				}
			}
			System.out.println(div + " " + rem);
		}
		}
	static boolean isPrime(int n) {
		boolean check = true;
		for (int i = 2; i <= Math.sqrt(n); i++) { // n이 2이상에서 나눠 떨어지면 소수가 아니다.
			if (n % i == 0)
				check = false; // 소수면 true 리턴
		}
		return check;
	}
	}

