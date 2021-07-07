# List indexing
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3])
print(a[-1])

# triple inner
b = [1, 2, ['a', 'b', ['Life', 'is']]]
print(b[2][2][0])

# List 연산
c = [1, 2, 3]
d = [4, 6, 5]
print(c + d)
print(c * 3)
print(len(c))

print(str(c[2]) + "hi")

# 리스트 요소 삭제 del 객체, remove, pop
del c[1]
print(c)

d.sort()
d.reverse()

print(d)

# 위치 반환
print(a.index(1))

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
a.extend(b)
print(a)


