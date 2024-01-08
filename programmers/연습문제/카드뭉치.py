def solution(cards1, cards2, goal):
    for i in goal:
        count = 0
        if len(cards1) != 0 and cards1[0] == i:
            cards1.pop(0)
            count += 1
        if len(cards2) != 0 and cards2[0] == i:
            cards2.pop(0)
            count += 1
        if count == 0:
            return "No"
    return "Yes"