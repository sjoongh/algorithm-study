def solution(scores):
    result  = ''
		
		# 각 학생에게 평가된 점수를 리스트 s로 변환
    for i in range(len(scores)):
        s = []
        for j in range(len(scores)):
            # 각 학생들이 받은 점수는 세로 열이므로
            # 자신이 받은 점수만 넣어줌[j][i]를 통해
            s.append(scores[j][i])
		# 자기 자신이 부여한 점수가 유일한 최고점 or 최저점 일 시
        # 제거해줌 ex : [0][0], [1][1] 검사 시
        # s[i]로 자기 자신만 검사함, 이차원배열을 s[i]로 일차원배열로 호출할 경우
        # 열과 행이 s[i]로 통일됨
        # --> 이차원 배열로 [0][0],[1][1]을 하지 않아도 자기자신을 검사할 수 있음
        if s[i] == min(s) and s.count(s[i]) == 1:
            del s[i]
        elif s[i] == max(s) and s.count(s[i]) == 1:
            del s[i]
        # 위 조건에 배제된 조건을 제외하고 평균을 구함
        mean = sum(s) / len(s)
				
				# 학점 변환
        if mean >= 90: result += 'A'
        elif mean >= 80: result += 'B'
        elif mean >= 70: result += 'C'
        elif mean >= 50: result += 'D'
        else: result += 'F'
    return result