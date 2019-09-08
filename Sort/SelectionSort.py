# 선택 정렬
def selection_sort(my_list):
    for i in range(0, len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            min = my_list[i]
            temp = 0
            if my_list[j] < min:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp


some_list = [11, 3, 6, 4, 12, 2, 4, 1, 3, 4, 7, 9, 11, 13, 15, 10, 21, 40]
selection_sort(some_list)
print(some_list)

