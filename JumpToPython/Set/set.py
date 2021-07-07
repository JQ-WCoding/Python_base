# 집합 자료형으로 선언 set 은 중복을 허용하지 않는다. 순서가 없다
s = set("Hello")
print(s)

l1 = list(s)
print(l1)
print(l1[3])

t1 = tuple(s)
print(t1)
print(t1[1])

# 교집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
# s1 = {1,2,3,4,5,6}
s2 = {4, 5, 6, 7, 8, 9}

print(s1 & s2)
print(s1.intersection(s2))

# 합집합 구하기
print(s1 | s2)
print(s1.union(s2))

# 차집합 구하기
print(s1 - s2)
print(s1.difference(s2))

# 값 1개 추가하기
s1 = {1, 2, 3}
s1.add(4)

print(s1)

# 값 여러개 추가하기
s1 = {1, 2, 3}
s1.update([4, 5, 6])
print(s1)

s1.remove(4)
print(s1)