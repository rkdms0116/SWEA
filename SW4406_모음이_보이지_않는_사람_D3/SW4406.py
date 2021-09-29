T = int(input())

vowel = ['a', 'e', 'i', 'o', 'u']
for t in range(T):
    test_str = str(input())
    show_str = '' # 보여질 문자열

    for alpha in range(len(test_str)):
        if test_str[alpha] not in vowel: # 모음에 없다면
            show_str += test_str[alpha] # 보여질 문자열에 더하여 줌
    
    print('#{} {}'.format(t+1, show_str))