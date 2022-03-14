package 2022-03-13;

class Solution {
    public int solution(int[] gold_prices) {
        
        int size = gold_prices.length;
        int[] dp = new int[size];

        for(int i = 0; i < size; i++) {
            for(int j = 0; j < i; j++) {
                if(gold_prices[i] - gold_prices[j] > 0) {
                    if(j >= 2) {
                        dp[i] = Math.max(dp[i], dp[j - 2] + gold_prices[i] - gold_prices[j]);
                    }
                      else {
                          dp[i] = gold_prices[i] - gold_prices[j];
                      }
                }
            }
        }

        int max = 0;
        for(int i = 0; i < size; i++) {
            max = Math.max(max, dp[i]);
        }
        return max;
    }
}