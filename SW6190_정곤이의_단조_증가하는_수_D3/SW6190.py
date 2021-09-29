import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    li =list(map(int, input().split()))

    mul = []
    for i in range(N-1):
        for j in range(i+1, N):
            mul.append(li[i]*li[j])

    result = -1
    mul.sort(reverse=True)

    for m in mul:
        num = str(m)
        if len(num) > 1:
            l = len(num)
            for j in range(l-1):
                if num[j] > num[j+1]:
                    break
            else:
                if result < m:
                    result = m

    print('#{} {}'.format(tc,result))