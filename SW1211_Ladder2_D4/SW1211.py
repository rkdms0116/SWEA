import sys
sys.stdin = open('input.txt')

def lad_cnt(arr):
    start = []
    for i in range(100):
        if arr[0][i] == 1:
            start.append(i)
    
    min_start = start[0]
    min_cnt = 99999
    
    for j in range(len(start)):
        y=0
        x=start[j]
        
        dx = [0, 1, -1]
        dy = [1, 0, 0]
        dir = 'down'

        cnt = 0

        while y < 99:
            if dir == 'down':
                x += dx[0]
                y += dy[0]

                if x < 99 and arr[y][x+1] == 1:
                    dir = 'right'

                if x > 0 and arr[y][x-1] == 1:
                    dir = 'left'

            if dir == 'right':
                x += dx[1]
                y += dy[1]

                if arr[y+1][x] == 1:
                    dir = 'down'

            if dir == 'left':
                x += dx[2]
                y += dy[2]

                if arr[y+1][x] == 1:
                    dir = 'down'
            cnt += 1
        
        if min_cnt > cnt:
            min_cnt = cnt
            min_start = start[j]
    return min_start



for _ in range(10):
    tc = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]
    print('#{} {}'.format(tc, lad_cnt(array)))