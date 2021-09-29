import sys
sys.stdin = open('input.txt')

def sudoku(arr):
    # row sudoku check
    for i in range(9):
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for j in range(9):
            if arr[i][j] in num_list:
                num_list.remove(arr[i][j])
            else:
                return 0

    # col sudoku check
    for i in range(9):
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for j in range(9):
            if arr[j][i] in num_list:
                num_list.remove(arr[j][i])
            else:
                return 0

    # 3by3 check
    for i in range(0,9,3):
        for j in range(0,9,3):
            num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for k in range(3):
                if arr[i+k][j+k] in num_list:
                    num_list.remove(arr[i+k][j+k])
                else:
                    return 0
    return 1

T = int(input())
for test in range(T):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))
    print(test+1, arr)
    result = sudoku(arr)
    print('#{} {}'.format(test+1, result))