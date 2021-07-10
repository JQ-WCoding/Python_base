import re

# ab 뒤에 아무거나 올 수 있는 정규식 객체를 만들어준다
p1 = re.compile('ab*')

p = re.compile('[a-z]+')

m = p.match("python")
print(m)

# 하지만 문자열 처음에 나오지 않으면 none 발생 match : 문자열 처음부터 검색
m = p.match("3 python")
print(m)

# search : 문자열 전체 검색
m = p.search("python")
print(m)
m = p.search("3 python")
print(m)

# findall : 전부 찾아서 리스트로 반환
result = p.findall("life is too short")
print(result)

# finditer
result = p.finditer("life is too short")
print(result)

# match 의 함수
m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

# 모듈 단위 수행
p = re.compile('[a-z]+')
m = p.match("python")
print(m)

m = re.match("[a-z]+", "python")
print(m)
