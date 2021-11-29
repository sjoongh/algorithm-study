def solution(s):
    # 공백을 기준으로 나눔
    s_split = s.split(' ')
    # 공백을 기준으로 나눈 각각의 요소 출력
    for i in range(len(s_split)):
        # 리스트 형식으로 만듬
        s_list = list(s_split[i])
        for j in range(len(s_list)):
            if j % 2 == 0:
                s_list[j] = s_list[j].upper()
            elif j % 2 != 0:
                s_list[j] = s_list[j].lower()
        # 정수형을 따로 배열에 삽입했으므로  '문자'형식으로 저장되는걸 방지하기 위해
        # join은 반복 자료형의 데이터를 하나의 문자열로 만듬
        # 하나의 문자열로 만들므로 각 문자를 의미하는 ''은 자동으로 사라지고
        # 구분자를 공백없이 "".join으로 설정했기 때문에 모든 문자가 붙어서 하나의 문자열이 출력됨
        s_split[i] = "".join(s_list)
    # 하나의 문자열로 구분되었다면 s_split의 각 요소들을 화이트스페이스로 구분지어줌
    answer = " ".join(s_split)
    return answer
