from itertools import permutations

def solution(numbers):

    nums = []
    for i in range(1, len(numbers)+1):
        num_list = list(permutations(numbers, i))

        for j in set(num_list):
            num = []
            for k in j:
                num.append(k)
            nums.append(int(''.join(num)))

        s_nums = set(nums)
        answer = 0
        for j in s_nums:
            if j >= 2:
                flag = True
                for k in range(2, j):
                    if j % k == 0:
                        flag = False
                        break
                if flag:
                    answer += 1

    return answer

print(solution("011"))