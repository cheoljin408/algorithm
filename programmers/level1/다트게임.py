import re
def solution(dartResult):
    stack = []
    result = re.sub('10', 't', dartResult)
    list_result = list(result)
    for i, v in enumerate(list_result):
        if v == 't':
            list_result[i] = '10'

    for idx, val in enumerate(list_result):
        if val.isdigit():
            stack.append(int(val))
        if val.isalpha():
            if val == 'S':
                num = stack.pop()
                stack.append(num ** 1)
            elif val == 'D':
                num = stack.pop()
                stack.append(num ** 2)
            else: # T
                num = stack.pop()
                stack.append(num ** 3)
        if val == '#':
            num = stack.pop()
            stack.append(num * -1)
        if val == '*':
            if len(stack) == 1:
                stack[0] = stack[0] * 2
            elif len(stack) > 1:
                stack[-1] = stack[-1] * 2
                stack[-2] = stack[-2] * 2

    return sum(stack)

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))