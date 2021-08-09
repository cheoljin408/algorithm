# 유클리드 호제법
def GCD(x, y):
    while y:
        x, y = y, x%y
    return x

def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result

def solution(n, m):
    answer = []
    
    # 일반적인 방법
    # for i in range(min(n, m), 0, -1):
    #     if n%i == 0 and m%i ==0:
    #         answer.append(i)
    #         break
            
    # for i in range(max(n, m), (n*m) + 1):
    #     if i%n == 0 and i%m == 0:
    #         answer.append(i)
    #         break

    # 유클리드 호제법
    answer.append(GCD(n, m))
    answer.append(LCM(n, m))
    
    return answer

print(solution(3, 12))
print(solution(2, 5))