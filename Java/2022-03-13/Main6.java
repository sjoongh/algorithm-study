package 2022-03-13;

// 프로그래머스 사칙연산
class Solution {
    static int [][]dp;

    private static int maxvalue(String[] arr, int i, int j) {
        if (dp[i][j] != Integer.MIN_VALUE) return dp[i][j];
        if (i - 1 >= 1 && arr[i-1].equals("-")) {
            int result = Integer.MAX_VALUE;
            for (int k = i; k < j; k += 2) {
                if (arr[k+1].equals("-")) result = Math.min(result, maxvalue(arr, i, k) - maxvalue(arr, k+2, j));
                else result = Math.min(result, maxvalue(arr, i, k) + maxvalue(arr, k+2, j));
            }
            dp[i][j] = result;
        } else {
            int result2 = Integer.MIN_VALUE;
            for (int l = i; l < j; l += 2) {
                if (arr[l+1].equals("-")) result2 = Math.max(result2, maxvalue(arr, i, l) - maxvalue(arr, l+2, j));
                else result2 = Math.max(result2, maxvalue(arr, i, l) + maxvalue(arr, l+2, j));
            }
            dp[i][j] = result2;
        }
        return dp[i][j];
    }

    public int solution(String arr[]) {
        int n = arr.length;
        dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = Integer.MIN_VALUE; // int정수의 최소범위 집어넣음
            }
            if (i % 2 == 0) dp[i][i] = Integer.parseInt(arr[i]); // 2로 나누어질 경우 
        }
        return maxvalue(arr, 0, n-1);
    }
}