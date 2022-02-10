import sys

N = int(sys.stdin.readline())

members = []
for i in range(N):
    member = input().split()
    member.append(i)
    members.append(member)

members.sort(key=lambda x: (int(x[0]), x[2]))

for i in members:
    print(i[0], i[1])