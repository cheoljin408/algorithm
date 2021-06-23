import sys

n = int(sys.stdin.readline())

coins = [5, 2]
cnt = 0

if n != 6 and n > 3 or n == 2:
    for coin in coins:
        cnt += n // coin
        n = n%coin
        if n == 3 or n == 1:
            n += coin
            cnt -= 1
    print(cnt)
else:
    print(-1)