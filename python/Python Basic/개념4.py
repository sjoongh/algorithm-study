def deposit(balance, money):
    print("count {0} won".format(balance + money))
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print("출금 완료. 잔액은 {0}원입니다".format(balance - mnoey))


balance = 0
balance = deposit(balance, 1000)
print(balance)


# .items() : 딕셔너리의 모든 pari 출력
# .keys() : 딕셔너리 모든 key 출력
# .values() : 딕셔너리 모든 value 출력
