import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())

    farm = []
    for n in range(N):
        str_int = input()
        num_list = list([int(char) for char in str_int])
        farm.append(num_list)

    profit = 0
    for i in range(N):
        for j in range(N):
            profit += farm[i][j]

    mid = N//2

    for i in range(mid):
        for j in range(mid-i):
            profit -= farm[i][j]
            profit -= farm[N-1-i][N-1-j]
            profit -= farm[N-1-i][j]
            profit -= farm[i][N-1-j]

    print('#{} {}'.format(tc+1, profit))
