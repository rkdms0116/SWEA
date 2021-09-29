
switch_n = int(input())     # switch 개수

switch = list(map(int, input().split()))    # switch 리스트
switch.insert(0,3)  # switch 시작이 1부터이므로

student_n = int(input())    # 학생 수

li = []
for _ in range(student_n):
    s, r = map(int, input().split())  #1 3 // 2 3
    li.append([s,r])

for p in range(len(li)):
    a = li[p][0]
    b = li[p][1]
    print(a, b)
    if a == 1:      # 남학생
        for i in range(1, len(switch)):
            if i%b == 0:
                if switch[i]==1:
                    switch[i] =0
                else:
                    switch[i] =1

    else:           # 여학생
        n = min(b-1, len(switch)-1-b)
        t = 1
        while t < n+1:
            if t ==1:
                if switch[b] == 0:
                    switch[b] = 1
                else:
                    switch[b] = 0
                    break
            if switch[b-t] == switch[b+t]:
                if switch[b-t] == 1:
                    switch[b-t] = 0
                    switch[b+t] = 0
                elif switch[b-t] == 0:
                    switch[b-t] = 1
                    switch[b+t] = 1
                t += 1
            else:
                break
    print(switch)