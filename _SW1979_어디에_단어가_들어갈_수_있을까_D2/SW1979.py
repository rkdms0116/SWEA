import sys
sys.stdin = open('input.txt')

T = int(input())

for test in range(T):
    N, K = map(int, input().split())
    sudo = []
    for _ in range(N):
        sudo.append(list(map(int, input().split())))

    result = 0
    cnt = 0
    i = 0

    # 가로 탐색
    while i < N:
        result = 0
        cnt = 1
        for j in range(N-1):
            if sudo[i][j] == 1 and sudo[i][j + 1] == 1:
                cnt += 1
            else:
                cnt = 1
            if cnt == K:
                result += 1
        i += 1

    print(result)