import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    city = [list(char for char in input()) for _ in range(N)]

    delta = [[-1,0],[1,0],[0,1],[0,-1]]

    for y in range(N):
        for x in range(N):
            if city[y][x] == 'A':
                if y+1<N and city[y+1][x] =='H':
                    city[y+1][x] = 'X'
                if x+1<N and city[y][x+1] == 'H':
                    city[y][x+1] = 'X'
                if 0<x and city[y][x-1] == 'H':
                    city[y][x-1] = 'X'
                if 0<y and city[y-1][x] == 'H':
                    city[y-1][x] = 'X'
            if city[y][x] == 'B':
                if y+1<N and city[y+1][x] =='H':
                    city[y+1][x] = 'X'
                if y+2<N and city[y+2][x] == 'H':
                    city[y+2][x] ='X'
                if x+1<N and city[y][x+1] == 'H':
                    city[y][x+1] = 'X'
                if x+2<N and city[y][x+2] == 'H':
                    city[y][x+2] = 'X'
                if 0<x and city[y][x-1] == 'H':
                    city[y][x-1] = 'X'
                if -1<x and city[y][x-2] == 'H':
                    city[y][x-2] ='X'
                if 0<y and city[y-1][x] == 'H':
                    city[y-1][x] = 'X'
                if -1<y and city[y-2][x] == 'H':
                    city[y-2][x] = 'X'
            if city[y][x] == 'C':
                if y+1<N and city[y+1][x] =='H':
                    city[y+1][x] = 'X'
                if y+2<N and city[y+2][x] == 'H':
                    city[y+2][x] ='X'
                if y+3<N and city[y+3][x] == 'H':
                    city[y+3][x] = 'X'
                if x+1<N and city[y][x+1] == 'H':
                    city[y][x+1] = 'X'
                if x+2<N and city[y][x+2] == 'H':
                    city[y][x+2] = 'X'
                if x+3<N and city[y][x+3] == 'H':
                    city[y][x+3] = 'X'
                if 0<x and city[y][x-1] == 'H':
                    city[y][x-1] = 'X'
                if -1<x and city[y][x-2] == 'H':
                    city[y][x-2] ='X'
                if -2<x and city[y][x-3] == 'H':
                    city[y][x-3] ='X'
                if 0<y and city[y-1][x] == 'H':
                    city[y-1][x] = 'X'
                if -1<y and city[y-2][x] == 'H':
                    city[y-2][x] = 'X'
                if -2<y and city[y-3][x] == 'H':
                    city[y-3][x] = 'X'
    cnt = 0
    for y in range(N):
        for x in range(N):
            if city[y][x] =='H':
                cnt +=1

    print(cnt)

'''
from pprint import pprint
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    cnt = 0

    for r in range(N):
        for c in range(N):

            if arr[r][c] == 'A':
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == 'H':
                            arr[nr][nc] = 'X'

            if arr[r][c] == 'B':
                for i in range(4):
                    for j in range(2):
                        nr = r+dr[i]*(j+1)  # dr, dc에 *2
                        nc = c+dc[i]*(j+1)
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] == 'H':
                                arr[nr][nc] = 'X'

            if arr[r][c] == 'C':
                for i in range(4):
                    for j in range(3):
                        nr = r+dr[i]*(j+1)
                        nc = c+dc[i]*(j+1)
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] == 'H':
                                arr[nr][nc] = 'X'

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 'H':
                cnt += 1

    print(cnt)
'''