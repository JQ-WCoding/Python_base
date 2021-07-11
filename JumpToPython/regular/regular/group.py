import re

# | 의 의미
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

# ^ 의 의미
# 맨 처음과 일치해야한다
print(re.search('^Life', 'Life is too short'))
# 안되는 경우
print(re.search('^Life', "My Life"))

# $ 의 의미
# 끝나는 경우
print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))

# \b (Word boundary) whitespace 에 의해 구분된다
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))

# \B 반대
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))

# grouping
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group())
