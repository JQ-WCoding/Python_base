# sample
money = True

if money:
    print("get taxi")
else:
    print("walk")

money = 3000

if money > 3000:
    print("get taxi")
else:
    print("walk")

# 비교연산 && || 등 사용 불가
if money == 3000 and money != 0:
    print(True)

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

pocket = ['money', 'cellphone', 'money']
if 'money' in pocket:
    print("get taxi")
else:
    print("walk")

# 조건문에서 아무것도 실행하지 않으려면 pass
if 'money' in pocket:
    pass
else:
    print("show ur card")

# 일반적인 조건문
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("get taxi")
else:
    if card:
        print("get taxi")
    else:
        print("walk")

# elif = else if 와 같은 의미
if 'money' in pocket:
    print("get taxi")
elif card:
    print("get taxi")
else:
    print("walk")


# 조건부 표현식
score = 80
message = "success" if score > 90 else "failure"
print(message)
