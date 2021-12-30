while(True):
    li = []
    s = input()
    # 힌트 : 7번째의 " ."와 같이 괄호가 하나도 없는 경우도 균형잡힌 문자열로 간주할 수 있다.
    if s == '.': # 때문에 'yes'라고 따로 출력문을 선언하지 않아도 무관, .이 나오면 반복문 종료 
        break
    for i in s:
        if i == '(' or i == '[': # 시작 괄호가 존재하면
            li.append(i) # 넣어줌
        elif i == ')': # 닫는괄호가 존재하면
            if len(li) == 0: # ???
                li.append('.')
                break
            elif li[-1] != '(': # 올바른 문자열인지 확인
                break
            else:
                li.pop() # 올바른 문자열이므로 제외
        elif i == ']': # 닫는괄호가 존재하면
            if len(li) == 0:
                li.append('.')
                break
            if li[-1] != '[':
                break
            else:
                li.pop()
    if li:
        print("no")
    else:
        print("yes")