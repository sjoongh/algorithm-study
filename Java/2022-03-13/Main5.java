package 2022-03-13;

// gold_prices : [2,5,1,3,4]
// result : 4
// 금 한 돈의 시세가 [2,4,1,3,4]일 때 최대 이익을 구하시오
// 이익이 발생하지 않으면 팔지 않아도 되며
// sell을 한 다음날은 buy할 수 없습니다.

class Solution {
    public int solution(int[] gold_prices) {
        
        int size = gold_prices.length;
        int[] dp = new int[size];

        for(int i = 0; i < size; i++) {
            for(int j = 0; j < i; j++) {
                if(gold_prices[i] - gold_prices[j] > 0) { // 이익이 발생하지 않으면 sell하지 않기 위한 조건
                    if(j >= 2) { // todo : 3일차 까지의 금을 비교해야함
                        dp[i] = Math.max(dp[i], dp[j - 3] + gold_prices[i] - gold_prices[j]);
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