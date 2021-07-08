# sample
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("%d 만큼 치다" % treeHit)
    if treeHit == 10:
        print("끝!")

prompt = """
        1. Add
        2. Del
        3. List
        4. Quit
        
        Enter num : """

number = 0
while number != 4:
    print(prompt)
    number = int(input())

# 홀수만 출력하기
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)
