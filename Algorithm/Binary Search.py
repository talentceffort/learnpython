def binary_search(element, some_list):
    # 코드를 작성하세요.
    start_index = 0;
    end_index = len(some_list) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2

        if some_list[mid_index] > element:
            end_index = mid_index - 1
        elif some_list[mid_index] < element:
            start_index = mid_index + 1
        else:
            return mid_index

    return None




print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))