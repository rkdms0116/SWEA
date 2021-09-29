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
        w.append(M - flag[i].count('W'))
        r.append(M - flag[i].count('R'))
        b.append(M - flag[i].count('B'))

    change = []
    cnt = 0
    for x in range(1, N-1):
        for y in range(x+1, N):
            cnt += sum(w[:x])
            cnt += sum(b[x:y])
            cnt += sum(r[y:])
            change.append(cnt)
            cnt = 0
    print('#{} {}'.format(tc,min(change)))
