# 파이썬의 모듈은 소문자를 권장한다
coffee = 10
while True:
    money = int(input("Insert your money"))
    if money == 300:
        print("Here's ur coffee")
        coffee -= 1
    elif money > 300:
        print("Here's your change %d" % (money - 300))
        coffee -= 1
    else:
        print("Sry, you can't buy coffee")
        print("%d coffee left" % coffee)

    if coffee == 0:
        print("There's no coffee left")
        break
