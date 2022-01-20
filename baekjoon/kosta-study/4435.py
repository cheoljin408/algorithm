t = int(input())

for i in range(t):
    g = list(map(int, input().split(' ')))
    s = list(map(int, input().split(' ')))

    gandalf_sum = g[0] + g[1]*2 + g[2]*3 + g[3]*3 + g[4]*4 + g[5]*10
    sourone_sum = s[0] + s[1]*2 + s[2]*2 + s[3]*2 + s[4]*3 + s[5]*5 + s[6]*10

    if gandalf_sum > sourone_sum:
        print('Battle {}: {}'.format(i+1, 'Good triumphs over Evil'))
    elif gandalf_sum < sourone_sum:
        print('Battle {}: {}'.format(i+1, 'Evil eradicates all trace of Good'))
    else:
        print('Battle {}: {}'.format(i + 1, 'No victor on this battle field'))