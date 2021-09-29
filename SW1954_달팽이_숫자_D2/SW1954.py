import sys
sys.stdin = open('input.txt')

def dalpang(N):
    # 우하좌상
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    dal = [[0]*N for _ in range(N)]

    x = y = 0
    num = 1
    dal[x][y] =1

    while num < N**2:
        if x+1 < N and dal[y][x+1] == 0:
            x += dx[0]
            y += dy[0]

        elif y+1 < N and dal[y+1][x] == 0:
            x += dx[1]
            y += dy[1]

        elif x > 0 and dal[y][x-1] == 0:
            x += dx[2]
            y += dy[2]

        elif y > 0 and dal[y-1][x] == 0:
            x += dx[3]
            y += dy[3]

        num += 1
        dal[y][x] = num
    return dal



T = int(input())

for tc in range(T):
    N = int(input())

    print('#{}'.format(tc+1))
    for snail in dalpang(N):
        print(*snail)