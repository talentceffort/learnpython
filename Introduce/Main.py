# sns의 유저
class User:
    # 초기값 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # 자기 소개 (이름, 이메일)
    def introduce(self):
        # 코드를 입력하세요.
        print("My name is " + self.name)
        print("My email address is " + self.email)

    # 자기 소개 두번
    def introduce_twice(self):
        self.introduce()
        self.introduce()
        # 코드를 입력하세요.

# 테스트
user1 = User("Young", "young@codeit.kr", "123456")
user1.introduce()
user1.introduce_twice()
