Test_Case = int(input())
for i in range(Test_Case):
    Test_words = str(input())
    while len(Test_words) >1:
        if Test_words[0] == Test_words[len(Test_words)-1]:
            Test_words = Test_words[1:len(Test_words)-1]
        else:
            result = 0
            break
        result = 1
    print(f'#{i+1} {result}')
