def solution(numbers, hand):
    answer = ''
    Left = 10
    Right = 12
    
    for n in numbers:
        if n in [1,4,7]:
            answer +='L'
            Left = n
        elif n in [3,6,9]:
            answer+='R'
            Right = n
        else:
            # n이 11이라면 0으로 만듬, 아니라면 그대로
            # 0을 11로 표현, 3배수를 위해
            n = 11 if n == 0 else n
            absL = abs(n-Left)
            absR = abs(n-Right)
            
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer +='R'
                Right = n
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer +='L'
                Left = n
            else:
                if hand == 'left':
                    answer +='L'
                    Left = n
                else:
                    answer+='R'
                    Right = n
                
    return answer