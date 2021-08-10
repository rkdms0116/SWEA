Test_case = int(input())

for test in range(Test_case):
    r_str = str(input())
    str_list = []
    for stri in r_str:
        str_list.append(stri)
    
    repeat_num = 0
    part_str = r_str[:2] # 앞의 글자 두개가 반복되면 같은 글자로 인정
    for rng in range(2,30,1):  
        if part_str == r_str[rng:rng+2]:
            repeat_num = rng
            break

    print(repeat_num)
