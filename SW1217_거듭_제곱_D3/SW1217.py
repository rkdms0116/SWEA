def expo(N, M):
    if M == 0:
        return 1
    return N * expo(N, M-1)

for _ in range(10):
    test = int(input())
    N, M = map(int, input().split())
    
    print('#{} {}'.format(test, expo(N, M)))
