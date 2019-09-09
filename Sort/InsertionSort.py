# 삽입 정렬
def insertion_sort(my_list):
    # 코드를 입력하세요.

    for i in range (1, (len(my_list))):
        temp = my_list[i]
        j = i - 1;
        while j >= 0 and temp < my_list[j]:
            my_list[j + 1] = my_list[j]
            j = j - 1
        my_list[j + 1] = temp
    return my_list



some_list = [11, 3, 6, 4, 12, 1, 2]
insertion_sort(some_list)
print(some_list)