# 자리수 합 리턴
def sum_digit(num):
    sum = 0
    str_num = str(num)
    for digit in str_num:
        sum += int(digit)
    return sum

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
total = 0
for num in range(1, 1001):
    print(sum_digit(num))
    total += sum_digit(num)

print(total)

