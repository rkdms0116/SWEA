T = int(input())

for t in range(T):
    L, U, X = map(int,input().split())

    if X > U:
        result = -1
    elif L < X < U:
        result = 0
    else:
        result = L-X
    
    print('#{} {}'.format(t+1, result))