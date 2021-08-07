
# Test_case = int(input())
# for i in range(Test_case):
#     Test_num = int(input())
#     cnt = 1
#     Num_list = ['1','2','3','4','5','6','7','8','9','0']
#     while len(Num_list)>0:
#         Num_split = []
#         for j in str(Test_num*cnt):
#             Num_split.append(j)
#         for k in Num_split:
#             if k in Num_list:
#                 Num_list.remove(k)

#         cnt +=1
#     print(f'#{i+1} {Test_num*(cnt-1)}')


Test_case = int(input())
for i in range(Test_case):
    Test_num = int(input())
    cnt = 1
    Num_list = ['1','2','3','4','5','6','7','8','9','0']
    while len(Num_list)>0:
        Num_split = []
        for j in str(Test_num*cnt):
            Num_split.append(j)
        for k in Num_split:
            if k in Num_list:
                Num_list.remove(k)
        if len(Num_list) ==0:
            break
        cnt +=1
    print(f'#{i+1} {Test_num*(cnt)}')