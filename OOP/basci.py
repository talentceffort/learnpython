class User:
    pass

# User값들 생성
user1 = User()
user2 = User()

# 파이썬의 기본 자료형
print(type(7))
print(type(3.14))
print(type("hello"))
print(type([1, 2, 3, 4, 5]))

# 우리가 만든 자료형
print(type(user1))
print(type(user2))

# 다른 주소값.
print(user1 == user2)