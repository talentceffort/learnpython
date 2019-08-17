
#프로그램을 실행하면 "기회가 *번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: "가 출력됩니다.
# 총 4번의 기회가 주어지며, 사용자가 한 번 추측할 때마다 남은 기회 횟수가 줄어듭니다.
#정답을 맞추면, "축하합니다. *번만에 숫자를 맞추셨습니다."가 출력되고 프로그램은 종료됩니다.
#사용자가 입력한 수가 정답보다 작을 경우 "Up"이 출력되고, 입력한 수가 정답보다 클 경우 "Down"이 출력됩니다.
#정답이 틀렸으면 (1)번부터 다시 진행합니다. 만약 4번의 기회를 모두 사용했는데도 답을 맞추지 못했으면, "아쉽습니다. 정답은 *였습니다."가 출력되고
# 프로그램은 종료됩니다.


from random import randint
NUMBER = randint(1, 20);
count = 4

while(count > 0) :
    answer = input('기회가 %d번 남았습니다. 1~20 사이의 숫자를 맞춰보세요!' % (count))
    answer = int(answer)

    if(answer == NUMBER) :
        print('축하합니다. %d번만에 숫자를 맞추셨습니다.' % (5 - count))
        break;
    elif(answer < NUMBER) :
        print('UP')
    elif(answer > NUMBER) :
        print('DOWN')

    if(answer != NUMBER and count == 1) :
        print("아쉽습니다. 정답은 %d였습니다." % (NUMBER))
    count = count - 1
