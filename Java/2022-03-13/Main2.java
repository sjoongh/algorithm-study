package 2022-03-13;

// P : "<<<><"
// 로봇은 위 블록의 아무곳이나 들어갈 수 있음
// >< 같이 겹치는 영역을 만나면 빠져나올 수 없음
// 그러므로 <<< 같이 빠져나올 수 있는 출발점의 개수를 count(start, end)
public class Solution {
    // solution 
    // 1. 시작점 --> 빠져나오는 영역의 마지막부터 계산 <만 계산하면 되므로 >가 나오면 break
    // 2. 끝점 --> 시작점과 반대로 출력
    // 3. 시작점+끝점으로 빠져나올수 있는 개수를 모두 count
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