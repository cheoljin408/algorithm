def solution(price, money, count):
    pay = 0

    for i in range(count):
        pay += price * (i+1)

    return pay-money if pay>=money else 0

print(solution(3, 20, 4))