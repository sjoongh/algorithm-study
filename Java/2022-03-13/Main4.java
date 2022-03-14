package 2022-03-13;

class Solution {
    public static int maxday(int k, int[] arr) {
        int sum =0, lt = 0, rt = k;
        for(int i = 0; i < k; i++) sum += arr[i];
        int max = sum;
        while (rt < arr.length) {
            sum -= arr[lt++];
            sum += arr[rt++];
            if (sum > max) {
                max = sum;
            }
        }
        return max;
    }

    public int solution(int[] estimates, int k) {
        int answer = 0;   
        return maxday(k, estimates);
    }
}