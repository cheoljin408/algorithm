n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

first = nums[-1]
second = nums[-2]

print(first, second)

sum = 0

while True:
    for i in range(k):
        if m == 0:
            break
        sum += first
        m -= 1
    if m == 0:
        break
    sum += second
    m -= 1

print(sum)