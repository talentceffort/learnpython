numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18]

# 리스트 뒤집기
length = len(numbers)
for num in range(length - 1, int(length / 2), -1):
    temp = numbers[(length - 1) - num] #맨 첫번째 수
    print(temp, numbers[num])
    numbers[(length - 1) - num] = numbers[num]  # 제일 끝 수를 0번째 index 에 넣음.
    numbers[num] = temp


print("뒤집어진 리스트: " + str(numbers))