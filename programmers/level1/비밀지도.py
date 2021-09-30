def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        arr1[i] = format(arr1[i], 'b')
        arr2[i] = format(arr2[i], 'b')

    print(arr1)
    print(arr2)
    print()
    for i in range(n):
        if len(arr1[i]) < n:
            arr1[i] = '0'*(n-len(arr1[i])) + arr1[i]
        if len(arr2[i]) < n:
            arr2[i] = '0'*(n-len(arr2[i])) + arr2[i]

        bit_number = ''
        for j in range(n):
            if (arr1[i][j] == '1' and arr2[i][j] == '1') or (arr1[i][j] == '1' and arr2[i][j] == '0') or (arr1[i][j] == '0' and arr2[i][j] == '1'):
                bit_number += '#'
            else:
                bit_number += ' '
        answer.append(bit_number)
    print(answer)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))