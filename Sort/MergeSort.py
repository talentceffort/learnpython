# 두 리스트 합치기
def merge(list1, list2):
    result = []
    i = 0
    j = 0

    print(list1, list2)

    while i < len(list1) and j < len(list2):
        if list1[i] >= list2[j]:
            result.append(list2[j])
            j += 1
        else:
            result.append(list1[i])
            i += 1

    #print(list1, list2)

    # while i < len(list1):
    #     result.append(list1[i])
    #     i += 1
    #
    # while j < len(list2):
    #     result.append(list2[j])
    #     j += 1

    #개선된 소스
    result += list1[i:] + list2[j:]

    return result



# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) <= 1:
        return my_list

    length = int(len(my_list) / 2)

    left = my_list[:length]
    right = my_list [length:]

    return merge(merge_sort(left), merge_sort(right))



some_list = [11, 3, 6, 4, 12, 1, 2]
sorted_list = merge_sort(some_list)
print(sorted_list)