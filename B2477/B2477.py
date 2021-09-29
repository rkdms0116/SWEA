fruit = int(input())

vat = []
for c in range(6):
    a, b = map(int, input().split())
    vat.append(b)

max_a = vat[-1]
max_b = vat[0]
max_sum = max_a + max_b
max_index = 0

for i in range(0, 5):
    if max_sum < vat[i] + vat[i+1]:
        max_a = vat[i]
        max_b = vat[i+1]
        max_sum = vat[i] + vat[i+1]
        max_index = i+1

min_a = vat[(max_index+2)%6]
min_b = vat[(max_index+3)%6]

charm = (max_a * max_b - min_a * min_b) * fruit
print(charm)