import sys
sys.stdin = open('sample_input.txt')

def circle(N, M):
    cir_li = []

    # 초기 피자 판 설정
    for _ in range(N):
        cir_li.append(pizza.pop(0))


    while len(cir_li) != 1 and pizza:
        a = cir_li.pop(0)
        a //= 2
        if a == 0:
            cir_li.append(pizza.pop(0))
        else:
            cir_li.insert(0, pizza.pop(0))

    return cir_li

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    print(circle(N,M))