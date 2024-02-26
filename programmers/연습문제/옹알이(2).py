# 문제 설명
# 머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다. 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 1 ≤ babbling의 길이 ≤ 100
# 1 ≤ babbling[i]의 길이 ≤ 30
# 문자열은 알파벳 소문자로만 이루어져 있습니다.
# 입출력 예
# babbling	result
# ["aya", "yee", "u", "maa"]	1
# ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]	2
# 입출력 예 설명
# 입출력 예 #1
#
# ["aya", "yee", "u", "maa"]에서 발음할 수 있는 것은 "aya"뿐입니다. 따라서 1을 return합니다.
# 입출력 예 #2
#
# ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]에서 발음할 수 있는 것은 "aya" + "ye" = "ayaye", "ye" + "ma" + "woo" = "yemawoo"로 2개입니다. "yeye"는 같은 발음이 연속되므로 발음할 수 없습니다. 따라서 2를 return합니다.
# 유의사항
# 네 가지를 붙여 만들 수 있는 발음 이외에는 어떤 발음도 할 수 없는 것으로 규정합니다. 예를 들어 "woowo"는 "woo"는 발음할 수 있지만 "wo"를 발음할 수 없기 때문에 할 수 없는 발음입니다.
# ※ 공지 - 2024년 2월 20일 문제 지문의 오탈자가 수정되었습니다.

def solution(babbling):
    vowels = ["aya", "ye", "woo", "ma"]
    cnt = 0

    for word in babbling:
        for i in vowels:
            if i in word:
                if i*2 in word:
                    continue
                else:
                    word = word.replace(i, '')
        if not word:
            cnt += 1
    return cnt


print(solution(["mamaayaye"]))