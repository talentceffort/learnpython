from random import randint

# 파일 열기
in_file = open('vocabulary.txt', 'r')

# key 값 생성
vocab = {}
for line in in_file:
    data = line.strip().split(":")
    vocab[data[0]] = data[1]

keys = list(vocab.keys())
print(keys)

# 파일 랜덤으로 읽어오기.
while True:
    index = randint(0, len(keys) - 1)
    ko_word = keys[index]
    en_word = vocab[ko_word]

    answer = input("%s :" % (ko_word))

    if answer == 'q':
        break

    if en_word.strip() == answer.strip():
        print("맞았습니다!")
    else:
        print("틀렸습니다 정답은 %s입니다." % (en_word))

# 파일 닫기
in_file.close()