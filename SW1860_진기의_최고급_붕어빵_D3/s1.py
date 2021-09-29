import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):

    N,M,K = map(int, input().split()) # 사람 명수, M초당 K개 붕어빵
    time = list(map(int, input().split()))

    time.sort()

    result = 'Possible'
    for i in range(N):
        fish = (time[i]//M)*K - (i+1)
        if fish<0:
            result = 'Impossible'

    print('#{} {}'.format(tc, result))