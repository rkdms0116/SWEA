import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    clap = input()
    n = len(clap)
    cnt = 0
    stand = int(clap[0])

    if clap[0] == '0':
        cnt += 1
        stand = 1

    for i in range(2, n):
        stand += int(clap[i-1])

        if clap[i] != '0' and stand < i-1:
            cnt += i - stand
            stand = i

    print('#{} {}'.format(tc,cnt))