import re

# 정규식
data = """
    park 800905-1049118
    kim 700905-1059119
"""

result = []
# line 을 띄어쓰기로 구분
for line in data.split("\n"):
    # 결과 값을 넣을 곳
    word_result = []
    # word 로 한줄에서 공백으로 구분
    for word in line.split(" "):
        # 주민번호 길이 14자리 '-' 포함
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

# 정규식 사용시
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

