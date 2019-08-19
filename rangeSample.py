numbers = [2, 4, 6, 8, 10, 12, 14, 16]

for i in range(len(numbers)):
    print(i, numbers[i])



# for i range(3, 17, 33): n 부터 m - 1 까지의 범위, s 만큼 증가.
#   print(i) -> [3, 6, 9, 12, 15]

#거듭 제곱 구현
for i in range(0, 11, 1):
    print("%d^%d = %d" % (2, i, 2 ** i))


#구구단 모범 답안.
# 앞자리 (1단부터 9단까지)
for i in range(1, 10):
    # 뒷자리
    for j in range(1, 10):
        print("%d * %d = %d" % (i, j, i * j))

#구구단 내 풀이
# for dan in range(1, 10, 1):
#    for num in range (1, 10, 1):
#        print("%d * %d = %d" % (dan, num, dan * num))