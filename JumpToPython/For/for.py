# sample
test_list = ['one', 'two', 'three']

for i in test_list:
    print(i)

# 튜플로 출력하기
a = [(1, 2), (3, 4), (5, 6)]
for (first, second) in a:
    print((first, second))

marks = [90, 25, 67, 45, 80]
for x in marks:
    if x > 60:
        print("%d 학생은 pass" % (int(marks.index(x)) + 1))
    else:
        print("%d 학생은 fail" % (int(marks.index(x)) + 1))

for x in marks:
    if x < 60:
        continue
    print("good job")

# range 이용
a = range(1, 11)
number = 0
for num in a:
    number += num

print(number)

number = 0
# range 변경 합격 예제
marks = [90, 25, 75, 30, 47]
for num in range(len(marks)):
    number += marks[num]

print(number)

# 99단 만들기
for i in range(2, 10):
    for j in range(2, 10):
        print(i * j, end=" ")
    print('')

number = [x * y for x in range(2, 10)
          for y in range(2, 10)]
print(number)

# list 내포 사용하기
a = [1, 2, 3, 4]
result = []
for i in a:
    result.append(i * 3)

print(result)

# 더 간단하게
result = [num * 3 for num in a]
print(result)

# if 조건문도 추가
result = [num * 3 for num in a if num % 2 == 0]
print(result)
