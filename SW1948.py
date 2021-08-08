month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Test_Case = int(input())
for i in range(Test_Case):
    result = 0
    m1, d1 ,m2, d2 = map(int, input().split())
    if m1 == m2:
        result = d2-d1+1
    else:
        for j in month_list[m1:m2-1]:
            result += j
        result += month_list[m1-1]-d1+d2+1
    print(f'#{i+1} {result}')
