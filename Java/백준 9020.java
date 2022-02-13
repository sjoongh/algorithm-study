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
			
			int div, rem;
			div = n / 2;
			rem = n - div;
			
			while (true) {
				if (isPrime(div) && isPrime(rem)) {
					break;
				} else {
					div--;
					rem++;
				}
			}
			System.out.println(div + " " + rem);
		}
		}
	static boolean isPrime(int n) {
		boolean check = true;
		for (int i = 2; i <= Math.sqrt(n); i++) {
			if (n % i == 0)
				check = false;
		}
		return check;
	}
	}

