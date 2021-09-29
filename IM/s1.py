import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    led = list(map(int, input().split()))
    led.insert(0,0)

    origin = [0]*(N+1)
    cnt = 0

    for i in range(N+1):
        if origin[i] != led[i]:
            for j in range(i,N+1):
                if j%i == 0:
                    if origin[j] == 0:
                        origin[j] = 1
                    else:
                        origin[j] = 0
            cnt +=1

    print('#{} {}'.format(tc, cnt))