import random
import time

# Q1 문자열 바꾸기
a = 'a:b:c:d'

a = a.replace(':', '#')
print(a)

# Q2 딕셔너리 값 추출하기 'C'가 없는 경우 70을 출력하기
a = {'A': 90, 'B': 80}

print(a.get('C', 70))

# Q3
a = [1, 2, 3]

a = a + [4, 5]  # 주소가 달라진다
a.extend([4, 5])  # 주소값을 그대로 유지한다

# Q4 50점 이상 총합 구하기
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

total = 0
while A:
    num = A.pop()
    if num >= 50:
        total += num

print(total)


# Q5 피보나치 함수
def mySol(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return mySol(n - 2) + mySol(n - 1)


# sample
for i in range(10):
    print(mySol(i))

result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)

print(result)


def compress_string(s):
    _c = ""
    cnt = 0
    result1 = ""
    for c in s:
        if c != _c:
            _c = c
            if cnt:
                result1 += str(cnt)
                cnt = 1
            else:
                cnt += 1
    if cnt:
        result1 += str(cnt)
    return result1


print(compress_string("aaabbcccccca"))

dic = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D'}


def morse(src):
    result2 = []
    for word in src.split(" "):
        for char in word.split(" "):
            result2.append(dic[char])
        result2.append(" ")
    return "".join(result2)


print(morse('...... . ... .-.. . . '))
