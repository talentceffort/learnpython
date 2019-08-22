
# My Solution
def is_palindrome(word):
    count = 0
    for i in range(0, int(len(word) / 2)):
        if word[i] == word[len(word)- 1 - i]:
            count += 1

    return count == int(len(word) / 2)

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

print(is_palindrome("hannah"))
print(is_palindrome("lagerregal"))
print(is_palindrome("otto"))
print(is_palindrome("reittier"))
print(is_palindrome("reliefpfeiler"))
print(is_palindrome("rentner"))
print(is_palindrome("rotor"))

# Feedback
def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍이 일치
    return True






