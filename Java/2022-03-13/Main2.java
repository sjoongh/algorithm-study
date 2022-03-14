package 2022-03-13;

public class Solution {
    // 부등호를 만날때까지 시작과 끝에서 count를 진행한다.
    // return 값으로 전체 count값 돌려줌
    public int solution(String str) {
        int leftCount = 0;
        int rightCount = 0;

        for(int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i); // str쪼개서 ch에 문자 하나씩 넣음
            if( ch == '>') break; // '>'를 만나면 종료
            leftCount++; // '>'가 아니라면 ++
        }

        for(int i = str.length() - 1; i >= 0; i--) {
            char ch = str.charAt(i);
            if( ch == '<') break;
            rightCount++;
        }

        return leftCount + rightCount;
    }
}