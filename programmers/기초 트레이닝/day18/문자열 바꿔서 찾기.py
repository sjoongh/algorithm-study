def solution(myString, pat):
    answer = 0
    change_myString = ""
    for i in myString:
        if i == "A":
            change_myString +=  "B"
        else:
            change_myString +=  "A"
    change_myString.find(pat)
    return change_myString.count(pat)