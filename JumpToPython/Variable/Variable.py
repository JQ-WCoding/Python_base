# 튜플로 생성하기 ()는 생략가능
a, b = ('python', 'life')
c, d = 'python', 'life'
print(type(a))
print(type(c))

# 리스트로 생성하기 []
[e, f] = ['python', 'life']

print(id(a))
# 값 바꾸기
a, b = b, a
print(a)
print(id(a))
print(b)
