alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0:5])
print(alphabets_list[4:])
print(alphabets_list[:4])

alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0:5])
print(alphabets_string[4:])
print(alphabets_string[:4])

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list3)

print(len('Hello, World!'))

numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)

name = 'jaeik'
name[0] = 'K'
print(name) #에러 발생. 문자열과 list의 차이. 문자열은 값 변경 불가.

name2 = 'jae' + 'ik'
print(name2)