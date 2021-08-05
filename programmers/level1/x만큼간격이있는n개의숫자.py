# 첫 번째 풀이

# def solution(x, n):
#     answer = []
#     plus = x
#     while True:
#         answer.append(x)
#         if len(answer) == n:
#             return answer
#         x = x+plus

# 두 번째 풀이
def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x*i + x)
    return answer

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))