import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    flag = [input() for _ in range(N)]
    w = []
    r = []
    b = []

    for i in range(N):
        w.append(flag[i].count('W'))
        r.append(flag[i].count('R'))
        b.append(flag[i].count('B'))

    change = 0
    for i in range(M):
        if flag[0][i] != 'W':
            change += 1
        if flag[N-1][i] != 'R':
            change += 1

    b = []

    for j in range(1, N-1):
        cnt = 0
        for k in range(j, N-1):
            if flag[:j] != 'W':
                cnt += 1
            if flag[j:k] != 'B':
                cnt += 1
            if flag[k:] != 'R':
                cnt += 1
        b.append(cnt)
    print(b)