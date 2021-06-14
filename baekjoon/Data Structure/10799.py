import sys

string = list(sys.stdin.readline())
sum = 0
cut_left = 0
cut_right = 1

for idx, item in enumerate(string):
    if item == '(':
        cut_left += 1
    elif item == ')':
        cut_left -= 1
        if string[idx-1] == '(':
            sum += cut_left
        else:
            sum += cut_right

print(sum)