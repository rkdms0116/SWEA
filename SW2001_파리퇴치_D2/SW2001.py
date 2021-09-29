import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    fly = []
    for n in range(N):
        fly.append(list(map(int, input().split())))
    # fly = [list(map(int, input().split())) for _ in range(N)]

    die_fly = []

    for row in range(N-M+1):
        for col in range(N-M+1):
            die = 0
            for m in range(M):
                for n in range(M):
                    die += fly[row+m][col+n]
            die_fly.append(die)

    print('#{} {}'.format(tc+1, max(die_fly)))
