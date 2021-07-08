
from copy import copy

# 주소값이 동일한 복사 방법
a = [1, 2, 3]
b = a

print(a)
print(id(a))
print(b)
print(id(b))

# 값만 복사하는 방법 [:]
b = a[:]

print(a)
print(id(a))
print(b)
print(id(b))

# copy 모듈 사용
b = copy(a)

print(id(b))
print(b is a)