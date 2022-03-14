package 2022-03-13;

public class Solution {
    public int solution(String str) {
        int leftCount = 0;
        int rightCount = 0;

        for(int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if( ch == '>') break;
            leftCount++;
        }

        for(int i = str.length() - 1; i >= 0; i--) {
            char ch = str.charAt(i);
            if( ch == '<') break;
            rightCount++;
        }

        return leftCount + rightCount;
    }
}