import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    deck = list(map(str, input().split()))


    result = []
    if N%2: # deck이 홀수이면
        deck1 = deck[:N//2+1]
        deck2 = deck[N//2+1:]
        for i in range(N//2):
            result.append(deck1[i])
            result.append(deck2[i])
        result.append(deck1[-1])
    else:
        deck1 = deck[:N//2]
        deck2 = deck[N//2:]

        for i in range(N//2):
            result.append(deck1[i])
            result.append(deck2[i])

    perfect = ' '.join(result)
    print('#{} {}'.format(tc, perfect))
