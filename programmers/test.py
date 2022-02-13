def solution(data):
    print(data)
    answer = []
    q = []
    time = 0
    for i in range(len(data)):
        if data[i][1] == time:
            answer.append(data[i])
            count = 1
            for j in range(data[i][2]):
                time += 1
                if time == data[i+count][1]:
                    q.append(data[i+count])
                    count += 1




        print(time)
        print(answer)
        print(q)

print(solution([[1, 0, 5], [2, 2, 2], [3, 3, 1], [4, 4, 1], [5, 10, 2]]))