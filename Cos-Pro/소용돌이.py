def solution(n):
    answer = 0

    # arr = [[0 for _ in range(n)] for _ in range(n)]
    # dir = 0 # 방향 0 1 2 3 0 1 2 3
    # loop = n # 해당 방향으로 채우는 숫자 개수
    # r, c = 0, -1 # 좌표의 초기 값
    # dr = [0, 1, 0, -1] # 방향에 대한 r의 변량
    # dc = [1, 0, -1, 0] # 방향에 대한 c의 변량
    # num = 0

    arr = [[0]*n for _ in range(n)]
    dir = 0
    loop = n
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = 0
    y = -1
    num = 0

    while num < n**2:
        for _ in range(loop):
            x += dx[dir]
            y += dy[dir]
            num += 1
            arr[x][y] = num
        dir = (dir + 1) % 4
        if dir % 2 == 1:
            loop -= 1

    for i in range(n):
        answer += arr[i][i]

    return answer


n1 = 3
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")
