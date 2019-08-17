# 컴퓨터는 0과 9 사이의 서로 다른 세 숫자를 임의의 순서로 뽑습니다. 사용자는 컴퓨터가 뽑은 숫자의 값과 위치를 맞추려고 합니다.
#
# 컴퓨터는 사용자가 입력한 세 숫자에 대해서, 아래의 규칙대로 스트라이크(S)와 볼(B)의 개수를 알려줍니다.
#
# 숫자의 값과 위치가 모두 일치하면 S입니다.
# 숫자의 값은 일치하지만 위치가 틀렸으면 B입니다.
# 예를 들어 컴퓨터가 1, 2, 3을 생성하였는데, 사용자가 1, 3, 5를 입력하면, 1S(1의 값과 위치가 일치) 1B(3의 값만 일치)입니다.
# 기회는 무제한입니다. 하지만 몇번의 시도 끝에 맞췄는지 기록됩니다.
#
# 3S(세 숫자의 값과 위치를 모두 맞춘 경우)일 때 게임이 끝납니다.


#서로 다른 세 수 뽑기.
numbers = [];
from random import randint

n = 0
while(n < 3) :
    number = randint(0, 9)
    if(str(number) not in numbers) :
        numbers.append(str(number))
        n += 1

print("0 ~ 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")

count = 0

#맞출때까지 반복.
while(True) :
    n = 0
    answers = []
    strike = 0;
    ball = 0;
    print("세 수를 하나씩 차례대로 입력하세요.")

    #사용자 입력값 유효성 검사.
    while(n < 3) :
        answer = input("%d번째 수를 입력하세요" % (n + 1))
        print(answer)
        if (answer in answers):
            print("중복되는 수 입니다. 다시 입력해주세요.")
        elif (int(answer) > 9):
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        elif(answer not in answers) :
            answers.append(answer)
            n += 1

    #Ball, Strike 판별.
    i = 0
    while(i < len(numbers)) :
        if(answers[i] in numbers) :
            if(answers[i] == numbers[i]) :
                strike += 1
            else :
                ball += 1
        i += 1
    print("%dS %dB" % (strike, ball))

    if(strike == 3) :
        print("축하합니다. %d 번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (count + 1))
        break;

    count += 1

