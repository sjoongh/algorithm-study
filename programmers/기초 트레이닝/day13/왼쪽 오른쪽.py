# 문제 설명
# 문자열 리스트 str_list에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다. str_list에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면 해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를, 먼저 나오는 문자열이 "r"이라면 해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 return하도록 solution 함수를 완성해주세요. "l"이나 "r"이 없다면 빈 리스트를 return합니다.
#
# 제한사항
# 1 ≤ str_list의 길이 ≤ 20
# str_list는 "u", "d", "l", "r" 네 개의 문자열로 이루어져 있습니다.
# 입출력 예
# str_list	result
# ["u", "u", "l", "r"]	["u", "u"]
# ["l"]	[]
# 입출력 예 설명
# 입출력 예 #1
#
# "r"보다 "l"이 먼저 나왔기 때문에 "l"의 왼쪽에 있는 문자열들을 담은 리스트인 ["u", "u"]를 return합니다.
# 입출력 예 #2
#
# "l"의 왼쪽에 문자열이 없기 때문에 빈 리스트를 return합니다.
# for 문을 쓰기 싫어서 조건문으로만 풀려고 했는데 테스트 케이스 2개가 자꾸 실패해서 결국 답을 봄
# l이나 r 둘 중 하나만 들었을 경우를 생각했어야 했는데 이걸 생각 못해서 실패한것 같다..

# 풀이 1.
def solution(str_list):
    if "l" not in str_list and "r" not in str_list:
        return []
    elif "l" not in str_list:
        return str_list[str_list.index("r")+1:]
    elif "r" not in str_list:
        return str_list[:str_list.index("l")]
    elif str_list.index("l") < str_list.index("r"):
        return str_list[:str_list.index("l")]
    else:
        return str_list[str_list.index("r")+1:]

# 풀이 2. -> for 문 쓰는 방식
def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i] == "l":
            return str_list[:i]
        elif str_list[i] == "r":
            return str_list[i+1:]

    return []