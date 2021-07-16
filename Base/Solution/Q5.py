import random
import re
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

p = re.compile('[a-z]+')
m = p.search("5 python")
print(m.start() + m.end())

pat = re.compile("\d{3}[-]\d{4}[-]\d{4}")
# 그루핑 하기
pat2 = re.compile("(\d{3}[-]\d{4})[-]\d{4}")

s = """
    park 010-9999-9988
    kim 010-9909-7789
    lee 010-8789-7767
"""

result = pat.sub("\g<1>-####", s)

print(result)

# .com 과.net 해당되는 이메일 주소 매칭
pat3 = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat3.match("pahkey@gmail.com"))
print(pat3.match("kim@daum.net"))
print(pat3.match("lee@myhome.co.kr"))


def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10


print(chkDupNum("0123456789"))
print(chkDupNum("1234"))
print(chkDupNum("01234567890"))
print(chkDupNum("6789012345"))
print(chkDupNum("012322456789"))
