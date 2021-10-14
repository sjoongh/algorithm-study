#   모의고사문제
def solution(answers):
    answer = []
    count1 = 0
    count2 = 0
    count3 = 0
    x = [1, 2, 3, 4, 5]
    y = [2, 1, 2, 3, 2, 4, 2, 5]
    z = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # range(len(answers)) == answers랑 같음
    answers=[]
    for i in range(len(answers)):
        if answers[i] == x[i % 5]:
            count1 += 1
        if answers[i] == y[i % len(y)]:
            count2 += 1
        if answers[i] == z[i % len(z)]:
            count3 += 1

    mac = max(count1, count2, count3)

    if mac == count1:
        answer.append(1)
    if mac == count2:
        answer.append(2)
    if mac == count3:
        answer.append(3)
