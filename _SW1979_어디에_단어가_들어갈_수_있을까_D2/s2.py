import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        cnt_r = 0
        for j in range(N):
            if puzzle[i][j] ==1:
                cnt_r += 1
            else:
                if cnt_r == K:
                    ans += 1
                cnt_r = 0
        if cnt_r == K:
            ans += 1

    cnt_c = 0
    for j in range(N):
            if puzzle[j][i] ==1:
                cnt_c += 1
            else:
                if cnt_c == K:
                    ans += 1
                cnt_c = 0
        if cnt_c == K:
            ans += 1