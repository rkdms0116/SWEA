import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    omok = [input() for _ in range(N)]

    delta = [[1,0], [0,1], [1,1], [-1,1]]
    result = 'NO'

    for y in range(N):
        for x in range(N):
            if omok[y][x] == 'o':
                for i in range(4):
                    sy = y
                    sx = x
                    cnt = 0
                    while cnt < 5 :
                        sy += delta[i][1]
                        sx += delta[i][0]
                        if -1 < sy < N and -1 < sx < N and omok[sy][sx] == 'o':
                            cnt += 1
                        else:
                            break
                    if cnt == 4:
                        result = 'YES'

    print('#{} {}'.format(tc,result))