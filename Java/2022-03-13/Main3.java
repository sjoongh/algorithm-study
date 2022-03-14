package 2022-03-13;

import java.util.*;

class Solution {
    private static boolean visited[];
    private static int result = 0;
    private static int k = 0;
    private static int t = 0;

    private static void combination(int[] arr, int idx, int level,int sum) {
        
        if ( level >= k && sum <= t) {
            result += 1;
        }
        if ( level == arr.length) return;
        for(int i = idx; i < arr.length; i++) {
            combination(arr, i + 1, level + 1, sum + arr[i]);
        }
    }


    public int solution(int[] arr, int K, int T) {
        k = K;
        t = T;
        Arrays.sort(arr);
        visited = new boolean[arr.length];

        combination(arr, 0, 0,0); //index, count
        return result;
    }
}