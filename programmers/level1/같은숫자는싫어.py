def solution(arr):
    answer = []
    
    answer.append(arr[0])
    
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
    
    # i = 0
    
    # while True:
    #     if i == len(arr)-1:
    #         break
    #     if arr[i] == arr[i+1]:
    #         arr.pop(i+1)
    #         i = i
    #     else:
    #         i += 1
    
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))