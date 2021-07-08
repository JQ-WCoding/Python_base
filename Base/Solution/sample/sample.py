a = ["이유덕", "이재영", "권종표", "이재영", "박민호", "강상희", "이재영", "김지완", "최승혁", "이성연", "박영서", "박민호", "전경헌", "송정환", "김재성", "이유덕",
     "전경헌"]

count1 = 0
count2 = 0
count3 = 0

for i in a:
    if "김" in i:
        count1 += 1
    elif "이" in i:
        count2 += 1
    if "이재영" in i:
        count3 += 1

print(count1, count2)

print("이재영은 총 %d명 입니다." % count3)

# 중복을 제거한 이름
a = set(a)
print(a)

print(sorted(a))
