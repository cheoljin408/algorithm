def solution(arr):

    arr.pop(arr.index(min(arr)))
    if len(arr) == 0:
        return [-1]

    return arr

print(solution([4, 3, 2, 1]))
print(solution([10]))