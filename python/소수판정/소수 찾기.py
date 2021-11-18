def solution(numbers):
    answer = 0
    num_li = []
    test = []
    for i in numbers:
        num_li.append(i)
    num_li.sort(reverse = True)
    num_li = ''.join(num_li)
    for i in range(2, int(num_li)+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
                if count > 2:
                    break
        if count == 2:
            test.append(i)
    tests = []
    for k in num_li:
        tests.append(k)
    if tests in test:
        tests.append(num_li)
    print(tests)
    return answer