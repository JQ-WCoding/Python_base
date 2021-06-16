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
