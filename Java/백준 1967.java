 java.util.*;
import java.io.*;
 
class Main {
    static int stoi(String s) {
        return Integer.parseInt(s);
    }
 
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
 
        int n = stoi(st.nextToken());
        int k = stoi(st.nextToken());
 
        if(n >= k)
            System.out.println(n-k);
        else
            System.out.println(bfs(n, k));
    }
 
    static int bfs(int n, int k) {
        Queue<Integer> q = new LinkedList<Integer>();
        int[] subin = new int[100001];
 
        q.offer(n);
        subin[n] = 1;
 
        while(!q.isEmpty()) {
            int now = q.poll();
 
            for(int i=0; i<3; i++) {
                int next;
 
                if(i == 0)
                    next = now - 1;
                else if(i == 1)
                    next = now + 1;
                else
                    next = now * 2;
 
                if(next == k)
                    return subin[now];                
 
                if(0 <= next && next <= 100000) {
                    if(subin[next] == 0) {
                        q.offer(next);
                        subin[next] = subin[now] + 1;
                    }
                }
            }
        }
        return 0;
    }
}
