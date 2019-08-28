from random import randint

# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    # 코드를 입력하세요
    numbers = []
    count = 0
    while count != 6:
        number = randint(1, 45)
        if number not in numbers:
           numbers.append(number)
           count += 1

    numbers.sort()
    return numbers

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    winning_numbers = generate_numbers()

    while True:
        bonus_number = randint(1, 45)
        if bonus_number not in winning_numbers:
            winning_numbers.append(bonus_number)
            break

    return winning_numbers

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    correct = 0

    for i in range(0, len(list1)):
        if list1[i] in list2:
            correct += 1

    return correct
# 로또 등수 확인하기
def check(numbers, winning_numbers):
    # 코드를 입력하세요
    matchNumber = count_matching_numbers(numbers, winning_numbers)
    bonus = False

    # 보너스 번호 일치 여부 확인.
    for num in numbers:
        if num == winning_numbers[len(winning_numbers) - 1]:
            bonus = True

    if matchNumber == 6:
        return 1000000000
    elif matchNumber == 5 and bonus:
        return 50000000
    elif matchNumber == 5:
        return 1000000
    elif matchNumber == 4:
        return 50000
    elif matchNumber == 3:
        return 5000
    else:
        return 0