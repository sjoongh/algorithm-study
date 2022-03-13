import java.util.*;

class Solution {
    private static String reverseString(String str) {
        char[] arr = str.toCharArray();
        for(int i = 0; i < str.length() / 2; i++) {
            char ch = arr[i];
            arr[i] = arr[arr.length - 1 - i];
            arr[arr.length - 1 - i] = ch;
        }
        return new String(arr);
    }
    
    public String solution(String S, int[][] interval) {
        
        for(int i = 0; i < interval.length ; i++) {
            int startIdx = interval[i][0] - 1;
            int endIdx = interval[i][1];
            String subString = reverseString(S.substring(startIdx, endIdx));
            String startString = S.substring(0, startIdx);
            String endString = S.substring(endIdx);
            S = startString + subString + endString;
        }
        return S;
    }
}