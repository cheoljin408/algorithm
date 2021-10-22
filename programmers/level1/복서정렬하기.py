import collections


def solution(weights, head2head):
    answer = []
    n = len(weights)
    total_info = collections.defaultdict(list)
    total_info_list = []

    # ["NLWL","WNLL","LWNW","WWLN"]
    # 승률 = (이긴횟수/전체횟수)*100
    for i in range(n):
        fight_count = 0
        win_count = 0
        over_weight_win = 0
        for j in range(n):
            # W이거나 L(경기를 진행했을때)일 때
            if head2head[i][j] == 'W' or head2head[i][j] == 'L':
                fight_count += 1
                # 시합에서 이겼을 때
                if head2head[i][j] == 'W':
                    win_count += 1
        # 전체횟수가 0이면 승률이 없음
        if fight_count == 0:
            total_info[i].append(0)
        else:
            total_info[i].append((win_count / fight_count) * 100)

        # 나보다 몸무게가 높은 사람이랑 싸워서 이긴 횟수를 구하는 for
        for j in range(n):
            # 나보다 몸무게가 높은 사람이랑 싸워서 이겼을 때
            if head2head[i][j] == 'W' and weights[i] < weights[j]:
                over_weight_win += 1

        # total_info 딕셔너리에 over_weight_win, 몸무게 append
        total_info[i].append(over_weight_win)
        total_info[i].append(weights[i])

    # 정렬
    sorted_total_info = sorted(total_info, reverse=True, key=lambda x: (total_info[x][0], total_info[x][1], total_info[x][2]))

    print(sorted_total_info)

    for i in range(n):
        answer.append(sorted_total_info[i]+1)

    return answer


print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))
print(solution([145, 92, 86], ["NLW", "WNL", "LWN"]))
print(solution([60, 70, 60], ["NNN", "NNN", "NNN"]))