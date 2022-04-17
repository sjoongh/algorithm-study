import java.util.*;
import java.io.*;
public class Main { 
    static int n, m, map[][], count = 0; 
    public static void main(String[] args) throws IOException { 
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
        StringTokenizer st = new StringTokenizer(br.readLine()); 
        n = stoi(st.nextToken()); 
        m = stoi(st.nextToken()); 
        map = new int[n + 1][n + 1];
        for (int i = 0; i < m; i++) { 
            st = new StringTokenizer(br.readLine()); 
            int u = stoi(st.nextToken()); 
            int v = stoi(st.nextToken()); 
            map[u][v] = 1; map[v][u] = 1; 
        } 
        dfs(0, new int[3], 1); 
        System.out.println(count); 
    } 
    static void dfs(int saveIdx, int save[], int start) { 
        if (saveIdx == 3) { 
            if (map[save[0]][save[1]] == 1 || map[save[1]][save[2]] == 1 || map[save[0]][save[2]] == 1) return; 
            count++; 
            return; 
        } 
        for (int i = start; i <= n; i++) { 
            save[saveIdx] = i; 
            dfs(saveIdx + 1, save, i + 1); 
        } 
    } 
    static int stoi(String s) { 
        return Integer.valueOf(s); 
    } 
}
