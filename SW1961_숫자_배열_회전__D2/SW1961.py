import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):

    N = int(input())
    li = []
    ro_li = [['']*3 for i in range(N)]

    for n in range(N):
        li.append(list(map(int,input().split())))

    for i in range(N):      # 90도
        for j in range(N):
            ro_li[j][0] += str(li[N-1-i][j])
            ro_li[j][1] += str(li[N-1-j][N-1-i])
            ro_li[j][2] += str(li[i][N-1-j])

    print('#{}'.format(tc+1))
    for result in ro_li:
        print(*result)