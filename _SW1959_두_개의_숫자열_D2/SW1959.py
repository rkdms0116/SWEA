Test_Case = int(input())
for test in range(Test_Case):
    li1, li2 = map(int,input().split())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))

    if li2 < li1:
        list1 , list2 = list2, list1

    sum_list = []

    for i in range(li2-li1+1):
        sum_number =0
        for j in range(li1):
            sum_number += list1[j]*list2[i+j]
        sum_list.append(sum_number)
    
    print('#{} {}'.format(test+1, max(sum_list)))
