import sys
sys.stdin = open('input.txt')

def tel():
    cnt = 0
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for b in range(N):
        for a in range(N):
            if city[b][a] == 'A' or city[b][a] == 'B' or city[b][a] == 'C':
                y = b
                x = a
                flag = True
                while y < N - 1:
                    y += delta[1][1]
                    x += delta[1][0]
                    if city[y][x] == 'H':
                        flag = False
                        break
                y = b
                while y > -1:
                    y += delta[3][1]
                    x += delta[3][0]
                    if city[y][x] == 'H':
                        flag = False
                        break
                y = b
                while x < N - 1:
                    y += delta[0][1]
                    x += delta[0][0]
                    if city[y][x] == 'H':
                        flag = False
                        break
                x = a
                while x > -1:
                    y += delta[2][1]
                    x += delta[2][0]
                    if city[y][x] == 'H':
                        flag = False
                        break

                if flag:
                    cnt += 1
    return cnt


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    city = [list(char for char in input()) for _ in range(N)]


    print(tel())