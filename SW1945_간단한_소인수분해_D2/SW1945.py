Test_Case = int(input())
for i in range(Test_Case+1):
    N = int(input())
    a,b,c,d,e = 0,0,0,0,0
    while N%2 == 0:
        N /= 2
        a += 1
    while N%3 == 0:
        N /= 3
        b += 1
    while N%5 == 0:
        N /= 5
        c += 1
    while N%7 == 0:
        N /= 7
        d += 1
    while N%11 == 0:
        N /= 11
        e += 1
    print(f'#{i+1} {a} {b} {c} {d} {e}')