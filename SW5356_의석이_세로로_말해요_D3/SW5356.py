import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test in range(T):

    row_str = []
    for _ in range(5):
        char_list = [char for char in str(input())]
        row_str.append(char_list)

    col_str = ''

    for i in range(15):
        for j in range(5):
            try:
                col_str += row_str[j][i]
            except IndexError:
                pass

    print('#{} {}'.format(test+1,col_str))