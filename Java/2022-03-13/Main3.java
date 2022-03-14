package 2022-03-13;

import java.util.*;
// 금액이 순서대로 들어있는 배열이 존재
// 주어진 항목 중에서 k개 이상의 항목을 선택하여 새 보험상품 만듬
// 배열[2,5,3,8,1], k = 3, t = 11이 주어진 경우
// 3개 이상의 항목을 선택하는 방법은 총 16가지가 존재함
// 이 중 선택된 항목들의 보장 금액의 합이 11이하가 되는 경우는
// 6가지가 존재한다.
// 항목별 보장금액이 순서대로 들어있는 배열 arr과 k,t가 매개변수일때
// arr에서 k개 이상의 항목을 선택했을 때 금액 합이 t이하가 되는 경우의 수 
class Solution {
    private static int result = 0;
    private static int k = 0;
    private static int t = 0;

    // idx : idx로 인덱스 위치를 옮겨가며 level과 sum의 조건을 만족시킴
    // level : 재귀함수를 끝내기 위함, level == arr.length가 될 경우 탐색이 종료되었으므로 return
    // sum : sum한 값이 t(합)이하의 수가 되는 것을 확인하기 위함
    public static void combination(int[] arr, int idx, int level, int sum) {
        if (k <= level && t >= sum) result += 1;
        if (level == arr.length) return;
        for (int i = idx; i < arr.length; i++) {
            // idx는 모든 경우를 탐색해야 하므로 i+1(재귀)
            // level : 재귀로 들어간 함수(idx)가 종료된것을 구분하기 위해 level + 1
            // sum : idx가 탐색할때마다 경우의 수를 계산
            combination(arr, i+1, level+1, sum+arr[i]);
        }
    }

    public static int solution(int[] arr, int K, int T) {
        k = K;
        t = T;
        Arrays.sort(arr); // 모든 경우의수를 완전탐색해야 하므로 정렬
        combination(arr, 0, 0, 0);
        return result;
    }
}