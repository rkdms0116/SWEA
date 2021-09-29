import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(T):
    day = int(input())
    price = list(map(int, input().split()))

    max_cost = price[day-1]
    cost, cnt, bene = 0, 0, 0
    for i in range(day-2, -1, -1):
        if price[i] < max_cost:
            cnt += 1
            cost += price[i]
            if i == 0:
                bene += max_cost * cnt - cost
        else:
            bene += max_cost * cnt - cost
            max_cost = price[i]
            cost, cnt = 0, 0

    print('#{} {}'.format(test+1, bene))