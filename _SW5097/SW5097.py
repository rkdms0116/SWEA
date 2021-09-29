import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    que_li = list(map(int, input().split()))

    while M > 0:
        a = que_li.pop(0)
        que_li.append(a)
        M -= 1

    print('#{} {}'.format(tc+1, que_li[0]))