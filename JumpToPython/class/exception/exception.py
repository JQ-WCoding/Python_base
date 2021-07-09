try:
    4 / 0
    # Exception 도 사용 가능
except ZeroDivisionError as e:
    print(e)
finally:
    print("hi")

# 여러개의 에러
try:
    a = [1, 2]
    # 인덱싱 에러가 먼저 발생하기 때문에 ZeroDivisionError 는 실행되지 않는다
    print(a[3])
    4 / 0
except ZeroDivisionError as e:
    print("0으로 나눌수 없습니다")
    print(e)
except IndexError as e:
    print("인덱싱 에러")
    print(e)

try:
    a = [1, 2]
    print(a[3])
    4 / 0
    # 다중 오류 처리하는 방법
except (ZeroDivisionError, IndexError) as e:
    print(e)

try:
    age = int(input('나이를 입력하세요 : '))
except:
    print('입력이 정확하지 않습니다')
else:
    if age <= 18:
        print("미성년자")
    else:
        print("성인")
