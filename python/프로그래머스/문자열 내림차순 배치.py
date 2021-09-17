def solution(s):
    s_list = list(s)
    ascii = []
    ascii_list = []
    for i in s_list:
        ascii.append(ord(i))
    ascii.sort(reverse=True)
    ascii = list(map(int, ascii))
    for j in ascii:
        ascii_list.append(chr(j))
    ascii_list="".join(ascii_list)
    
    return ascii_list