import sys

N = int(sys.stdin.readline())
find = int(sys.stdin.readline())

if N == 1:
    print(1)
    print(0, 0)
else:
    arr = [[0] * N for _ in range(N)]
    arr[N//2][N//2] = 1
    arr[N//2 - 1][N//2] = 2
    x = N // 2 - 1
    y = N // 2
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir = 0
    loop = 1
    num = 2
    findx = 0
    findy = 0

    while num < N**2:
        for _ in range(loop):
            x += dx[dir]
            y += dy[dir]
            num += 1
            arr[x][y] = num
        dir = (dir + 1) % 4
        if dir % 2 == 1 and x != N-1:
            loop += 1

    for i in range(N):
        if find in arr[i]:
            findy = arr[i].index(find) + 1
            findx = i + 1
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
    print(findx, findy)
