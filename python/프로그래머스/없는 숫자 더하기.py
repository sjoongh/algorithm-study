def solution(price, money, count):
    answer = -1
    x = 0
    for i in range(2, count+1):
        money_count = price
        money_count = i * price
        x += money_count
    if (x + price) <= money:
        return 0
    return (x+price) - money
