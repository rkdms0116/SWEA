# 내 머리가 고생
Test_Case = int(input())
for i in range(Test_Case):
    Test_Num = int(input())
    if Test_Num%2:
        result = int((Test_Num+1)/2)
    else:
        result = int(-Test_Num/2)
    print(f'#{i+1} {result}')

# 컴퓨터가 고생
Test_Case = int(input())
for i in range(Test_Case):
    Test_Num = int(input())
    result_sum = 0
    for j in range(1,Test_Num+1):
        if j%2:
            result_sum += j
        else:
            result_sum -= j
    print(f'#{i+1} {result_sum}')