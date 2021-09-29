import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    income = list(map(int,input().split()))

    total = 0
    for i in range(N):
        total += income[i]
    av = total/N

    cnt = 0
    for j in range(N):
        if income[j] <= av:
            cnt += 1
    
    print('#{} {}'.format(tc, cnt))