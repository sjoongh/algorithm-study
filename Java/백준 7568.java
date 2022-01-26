import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int people[][] = new int[num][2];
		int rank[] = new int[num];
		
		for (int i = 0; i < num; i++) {
			people[i][0] = sc.nextInt();
			people[i][1] = sc.nextInt();
		}
		for (int i = 0; i < num; i++)
			for (int j = 0; j < num; j++)
				if (people[i][0] < people[j][0] && people[i][1] < people[j][1])
					rank[i]++;
		for (int i = 0; i < num; i++)
			System.out.print((rank[i] + 1) + " ");
	}
}