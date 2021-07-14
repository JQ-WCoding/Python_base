import re

# "abcabcabc" "abc"


str2 = "abcabcabc"


def mySol(line1, line2):
    conunt = 0
    for i in range(len(line1)):
        p2 = '.{%d}' % i
        p3 = p2.join(line2)
        answer1 = re.findall(r'(?=%s)' % p3, line1)
        for j in answer1:
            conunt += 1
    return conunt


print(mySol("abbbcbbb", "bbb"))
print(mySol("abcabcabc", "abc"))
print(mySol("abacaba", "acb"))
# 내가 추가로 궁금해서 만들어 본것
print(mySol("cccc", "ccc"))
