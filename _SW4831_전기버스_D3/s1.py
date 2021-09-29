import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(T):

    K, N, M = map(int,input().split())      # K : 최대 정류장, N : 종착역, M : 충전기 개수
    gas = list(map(int,input().split()))

    cnt = 0
    state = 0
    temp = 0

    while state < N:
        temp += K
        for stop in gas:
            while stop <= state:
                gas.remove(stop)
