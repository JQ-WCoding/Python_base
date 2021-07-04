# abs 절대값
print(abs(3))
print(abs(3.2))
print(abs(-4.5))

# all 모두가 참이면 true 하나라도 거짓이면 false
print(all([1, 2, 3]))
print(all([1, 2, 0]))

# any 하나라도 참이면 true 모두 거직이면 false
print(any([1, 2, 3]))
print(any([1, 2, 3, 0]))
print(any([0, ""]))

# chr 유니코드 입력받아 문자로 출력
print(chr(97))

# ord -> chr 반대 함수
print(ord('a'))

# dir 객체가 자체적으로 가지고 있는 변수나 함수
print(dir([1, 2, 3]))

# divmod 몫과 나머지를 출력해주는 함수
print(divmod(7, 3))

# 반복문
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# eval 실행 가능한 문자열 입력받아 문자열을 실행한 결과값
print(eval('1+2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4,3)'))


#  map
def two_times(x):
    return x * 2


print(list(map(two_times, [1, 2, 3, 4])))

# pow 제곱값
print(pow(2, 4))

# range 해당 범위 끝 수는 없는걸로
print(list(range(1, 10)))
print(list(range(0, -10, -1)))
print(list(range(0, 10, 2)))

# round 반올림
print(round(4.3))

# sorted 정렬
print(sorted([3, 1, 2]))

# str 문자열로 변환
print(str(316))

# sum 모든 리스트 튜플 합
print(sum([1, 3, 4]))

#  tuple 튜플로 전환 (, , , ,) 형태로 표시
print(tuple("abc"))

# type 자료형이 무엇인지
print(type("abc"))

# zip 동일한 개수로 이루어진 자료형을 묶어 주는 역할의 함수
print(list(zip([1, 2, 3], [4, 5, 6])))
