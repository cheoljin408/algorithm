N = int(input())

for _ in range(N):
    stck = []
    check = True
    string = input()

    for i in string:
        if i == '(':
            stck.append('(')
        elif i == ')':
            if len(stck) == 0:
                check = False
            else:
                stck.pop(-1)

    if check == False or len(stck) != 0:
        print('NO')
    else:
        print('YES')

        
    
