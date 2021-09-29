import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    E, N = map(int,input().split())
    li = [[0]*(E+1) for _ in range(2)]
    node = list(map(int, input().split()))

    for num in range(0,2*E,2):
        if li[0][node[num]]:
            li[1][node[num]] = node[num+1]
        else:
            li[0][node[num]] = node[num+1]
    print(li)
