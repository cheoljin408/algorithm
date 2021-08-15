def solution(s):
    s = list(s)
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    cnt = 0

    for i in range(len(s)):
        if s[i] in nums:
            cnt += 1

    if cnt == len(s) and (len(s) == 4 or len(s) == 6):
        return True
    else:
        return False


print(solution('a234'))
print(solution('1234'))