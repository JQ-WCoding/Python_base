# 여러개의 입력값을 받는 함수를 만들기
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result


print(add_many(1, 2, 3, 4, 5, 6))


# 여러개의 매개변수
def choice_func(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result


print(choice_func("add", 1, 2, 3, 4, 5))
print(choice_func("mul", 1, 2, 3, 4, 5))


# 키워드 파라미터 kwargs
def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(a=1)
print_kwargs(a=1, b=2, c=3)


# 함수의 결과값은 언제나 하나이다
def add_and_null(a, b):
    return a + b, a * b


result = add_and_null(3, 4)
print(result)

a, b = add_and_null(3, 4)
print(a, b)


# python 은 파라미터의 인덱스도 중요하다
def say_myself(name, old, man=True):
    print("나의 이름은 %s" % name)
    print("나의 나이는 %d" % old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")


say_myself("아아", 12)
say_myself("으으", 14, False)
