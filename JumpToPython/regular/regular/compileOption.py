# 정규식 컴파일 옵션
# DOTALL(S) IGNORECASE(I) MULTILINE(M) VERBOSE(X)

import re

p = re.compile('a.b')
m = p.match('a\nb')  # . 문자와 매치되지 않음
print(m)

p = re.compile('a.b', re.DOTALL)  # DOTALL을 통해 \n 문자도 가능하도록 파라미터 추가로 설정
m = p.match('a\nb')
print(m)

p = re.compile('[a-z]', re.I)  # IGNORECASE 를 이용해 대소문자 구분을 하지 않는다
p.match('python')
p.match('Python')
p.match('PYTHON')

p = re.compile("^python\s\w+")

data = """
    life is too short
    python two
    you need python
    python three
"""

print(p.findall(data))

p = re.compile("^python\s\w+", re.MULTILINE)

print(p.findall(data))

# VERBOSE, X
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]);')

# \ 백슬새시는 \section의 경우 \\section으로 해결 가능
# \\\\ RawString 규칙 적용시 \\section 과 같이 표현가능
p = re.compile(r'\\section')
