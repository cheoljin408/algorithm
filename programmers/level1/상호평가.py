def solution(scores):
    answer = ''
    n = len(scores)

    for i in range(n):
        nums = []
        for j in range(n):
            nums.append(scores[j][i])

        div = n
        total = sum(nums)
        if max(nums) == nums[i] and nums.count(nums[i]) == 1:
            total -= nums[i]
            div -= 1
        if min(nums) == nums[i] and nums.count(nums[i]) == 1:
            total -= nums[i]
            div -= 1

        avg = total / div

        if avg >= 90:
            answer += 'A'
        elif 80 <= avg < 90:
            answer += 'B'
        elif 70 <= avg < 80:
            answer += 'C'
        elif 50 <= avg < 70:
            answer += 'D'
        else:
            answer += 'F'

    return answer


print(solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77],
                [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))
print(solution([[50, 90], [50, 87]]))
print(solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]]))