# try catch 와 같은 표현
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

# 오류 실행
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
else:  # 오류가 없을 경우 실행
    print("오류 없음")

# 오류 결과
try:
    age = int(input('나이를 입력하세요 : '))
except Exception as e:
    print(e)
else:
    if age <= 18:
        print("미성년자입니다.")
    else:
        print("성인입니다.")

# 오류 회피하기 (오류 발생시 지나가기)
try:
    f = open("except", 'r')
except FileNotFoundError:
    pass


# 강제 오류 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError


# 오류 상속
class MyError(Exception):
    pass


def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
