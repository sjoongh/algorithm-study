# 문자를 큰 것 부터 아스키코드 순서대로 배치해야함
# 대문자는 가장 앞에 위치
def solution(s):
    s_list = list(s)
    ascii = []
    ascii_list = []
    for i in s_list:
        # 알파벳을 아스키코드 숫자값으로 변경 ord()
        ascii.append(ord(i))
    # 아스키코드 숫자로 되어있는 배열을 내림차순으로 정렬
    # 대문자가 숫자가 높으므로
    ascii.sort(reverse=True)
    # char값이었으므로 int형으로 변환
    ascii = list(map(int, ascii))
    for j in ascii:
        # 다시 알파벳으로 바꿔줌
        ascii_list.append(chr(j))
    # "".join으로 하나의 문자열로 만듬
    ascii_list="".join(ascii_list)

    return ascii_list