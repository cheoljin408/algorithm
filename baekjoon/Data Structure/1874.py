import sys

N = int(sys.stdin.readline())
nums = []
plus_num = 0
stck = []
answer = []
flag = True

for i in range(N):
    nums.append(int(sys.stdin.readline()))

for i in nums:
    while True:
        if i <= plus_num:
            break
        plus_num += 1
        stck.append(plus_num)
        answer.append('+')
    # print(stck)
    # print(answer)

    if i == stck[-1]:
        stck.pop()
        answer.append('-')
    
    else:
        flag = False

if not flag:
    print('NO')
else:
    print('\n'.join(answer))
