def solution(record):
    answer = []
    nickname = {} # 딕셔너리
    
    for r in record:
        row = r.split(' ')
        if row[0] == 'Enter' or row[0] == 'Change':
            # nickname 딕셔너리 { row[1]:key = row[2]:value } 형태로 삽입됨
            # 딕셔너리에 key값을 추가할때는 nickname[key] = value 처럼 사용
            nickname[row[1]] = row[2]  
    for r in record:
        row = r.split(' ')
        if row[0] == 'Enter':
            # nickname 딕셔너리에 row[1]에 해당하는 value + 'String'
            answer.append(nickname[row[1]] + '님이 들어왔습니다.')
        elif row[0] == 'Leave':
            answer.append(nickname[row[1]] + '님이 나갔습니다.')
    
    return answer