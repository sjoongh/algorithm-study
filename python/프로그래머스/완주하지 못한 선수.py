# # 완주하지 못한 선수
def solution(participant, completion):
    participant_set = set(participant)
    completion_set = set(completion)
    result = list(participant_set - completion_set)
    if result != []:
        return result[0]
    else:
        for c in completion:
            a = completion.count(c)
            b = participant.count(c)
            if(a != b):
                return c
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
               ["josipa", "filipa", "marina", "nikola"]))
