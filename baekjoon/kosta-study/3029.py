a1, b1, c1 = map(int, input().split(":"))
a2, b2, c2 = map(int, input().split(":"))

ans1 = a1 * 3600 + b1 * 60 + c1
ans2 = a2 * 3600 + b2 * 60 + c2

if ans1 >= ans2:
    ans2 += 3600 * 24

ans3 = ans2 - ans1
a3 = ans3 // 3600
ans3 %= 3600
b3 = ans3 // 60
ans3 %= 60
c3 = ans3
print("%02d:%02d:%02d" % (a3, b3, c3))