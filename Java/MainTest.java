import java.util.*;

class Solution {
    static int n;
    static ArrayList<Integer>[] list;
    static boolean[] visited;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        list = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            list[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            list[x].add(y);
            list[y].add(x);
        }
        for (int i = 0; i < n; i++) {
            visited = new boolean[n];
            dfs(i, 0);
        }
        System.out.println(0);
    }

    public static void dfs(int x, int len) {
        if (len == 4) {
            System.out.println(1);
            return;
        }
        visited[x] = true;
        for (int i = 0; i < list[x].size(); i++) {
            int tmp = list[x].get(i);
            if (visited[tmp] == false) {
                visited[tmp] = true;
                dfs(tmp, len+1);
                visited[tmp] = false;
            }
        }
    }
}