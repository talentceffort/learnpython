# 빈 리스트 만들기
numbers = []

# numbers에 자연수 1부터 10까지 추가
n = 0
while(n < 10) :
    numbers.append(n + 1)
    n = n + 1

print(numbers)

# numbers에서 홀수 제거
n = 0
while(n < len(numbers)) :
    if(numbers[n] % 2 != 0) :
        del numbers[n]
    else :
        n += 1 #원소가 제거될 때 index 가 줄어들어 모든 리스트이 값을 테스트 할 수 없으므로 이를 해결하기 위한 방법.
        #위 방법을 보완하기 위해서는 index 의 맨 뒤에서 지워나가면 깔끔하게 지워나갈 수 있다.

print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
numbers.sort()
print(numbers)