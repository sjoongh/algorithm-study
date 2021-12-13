def solution(citations):
    answer = 0
    citations.sort()
    lengths = len(citations)
    for i in range(len(citations)):
        hIndex = lengths - i
        
        if citations[i] >= hIndex:
            answer = hIndex
            break
    
    return answer