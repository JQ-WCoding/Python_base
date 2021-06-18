# 문자열 더하기
head = "Python"
tail = " is fun!"
wholeWord = head + tail
print(wholeWord)

# 문자열 곱하기
a = "Python"
print(a * 2)

# 응용
print("=" * 50)
print("My Python")
print("=" * 50)

# 문자열 길이 구하기 len() 띄어쓰기를 포함한다 (당연한 소리)
print(len(wholeWord))

# 문자열 인덱싱
word = "Life is too short, You need Python"
print(word[3])
# 뒤에서부터 시작 -0 은 0이기에 -1 부터 시작이다
print(word[-0])
print(word[-1])
# 합쳐서 단어 만들기 인덱스 0 ~ 3까지
print(word[0:4])
# 비슷한 예시
print(word[19:])
print(word[:17])
print(word[19:-7])

sample = "20210616Sunny"
date = sample[:8]
weather = sample[8:]
# 다중 출력도 가능
print(date, weather)

wrongWord = "pithon"
rightWord = wrongWord[:1] + 'y' + wrongWord[2:]
print(rightWord)

# 문자열 포매팅
sentence = "I eat %s apples"
print("I eat %d apples" % 3)
print(sentence % "five")

print("i ate %d apples. So, I was sick for %s days" % (3, "three"))

# 하지만 %s는 무적
print("i ate %s apples. So, I was sick for %s days" % (3, "three"))

# 포매팅 연산자가 있다면 뒤에 %를 표현하려면 %% 두번 사용해야함
print("%d%%" % 100)

# 정렬과 공백
# 10칸 띄어쓰기
print("%10s" % 'hi')
# 10칸 반대로 띄어쓰기
print("%-10sjane" % 'hi')

print("I eat {0} apples".format(3))

# 인덱스와 name 혼합
print("I ate {0} apples. So, I was sick for {day} days".format(10, day=3))
# {} 해당 번호는 인덱스 번호
print("I ate {0} apples. So, I was sick for {1} days".format(10, 3))

# :< :> 좌우정렬 :^ 가운데 정렬
print("{0:^10}".format("hi"))

# f'문자열' formatting 을 선언하고 표현할 수 있다
name = 'jun'
age = 28
print(f'나의 이름은 {name}이고, {age}살 입니다')

# 문자 개수 세기
text = "hobby"
print(text.count('b'))
# 인덱스 위치 찾기
print(text.find('h'))
# index는 문자열을 찾지 못하면 오류 발생
print(text.index('h'))

print(",".join('abcd'))