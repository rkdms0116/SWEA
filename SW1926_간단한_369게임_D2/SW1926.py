N = int(input())
num369 = ''
for i in range(1, N+1):
    cnt =0
    if i in range(1,10):
        if i%3 == 0:
            num369 += "- "
        else:
            num369 += str(i) + ' '
    else:
        j = str(i)
        cnt += j.count('3')
        cnt += j.count('6')
        cnt += j.count('9')
        if cnt==1: 
           num369 += '- '
        elif cnt==2:
            num369 += '-- ' 
        else:
            num369 += j +' '
print(num369[:len(num369)])
