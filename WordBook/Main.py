#파일 열기
out_file = open('vocabulary.txt', 'w')

# 파일에 쓰기

while True:
    en_word = input("영어 단어를 입력하세요")
    if en_word == 'q':
        break
    ko_word = input("한국 뜻을 입력하세요")

    out_file.write("%s : %s\n" % (en_word, ko_word))

# 파일 닫기
out_file.close()