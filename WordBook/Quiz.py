# 파일 열기
in_file = open('vocabulary.txt', 'r')

# 한 줄씩 읽어오고 정답 맞추기.
for line in in_file:
    en_word = line.strip().split(":")[0]
    ko_word = line.strip().split(":")[1]
    answer = input("%s :" % (ko_word) )

    if en_word.strip() != answer.strip():
        print("아쉽습니다 정답은 %s 입니다." % (en_word))
    else:
        print("맞았습니다!")


# 파일 닫기
in_file.close()

