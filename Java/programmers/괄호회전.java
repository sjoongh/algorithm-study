package programmers;

import java.util.Stack;

class Solution {
    public int solution(String s) {
        int result = 0;
        
        for (int i = 0; i < s.length(); i++) {
            // s를 왼쪽으로 회전해야 하므로
            // 1. 문자열 s의 첫번째 문자만 뽑아냄 -> s.substring(0,1)
            // 2. 나머지 문자들을 앞에서 더해줌 -> s.substring(1)
            // s.substring(1) + s.substring(0,1) --> 위의 방식으로 한칸씩 왼쪽으로 밀리는 결과가 나옴
            // 나머지는 check를 통한 검증
            s = s.substring(1) + s.substring(0,1);
            if (check(s)) result++; // true로 대응된 경우에만 + 1
        }
        return result;
    }
    public boolean check(String s) {
        // stack 사용
        // 닫는 괄호 먼저 나오면 return 0
        // charAt로 검증 닫는 괄호는 stack.peek로 다시 검증
        // peek : 스택의 최상단 데이터 확인
        // peek로 확인했을때 대응된다면 올바른 괄호이므로 현재 stack을 pop해줌
        // 대응되지 않는다면 false
        Stack<Character> stack = new Stack();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (stack.empty()) {
                stack.add(c);
            } else {
                if (c=='['||c=='('||c=='{') {
                    stack.add(c);
                } else {
                    if (c==']') {
                        if (stack.peek()!='[') return false;
                        else stack.pop();
                    } else if (c==')') {
                        if (stack.peek()!='(') return false;
                        else stack.pop();
                    } else if (c == '}') {
                        if (stack.peek()!='{') return false;
                        else stack.pop();
                    }
                }
            }
        }
        
        if (stack.size()!=0) { // 모든 stack이 대응되지 않았을 경우 false
            return false;
        }
        return true; // 검증이 끝나 stack을 0으로 만든 경우
    }
}