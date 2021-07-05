# Q1
def is_odd(num):
    if num % 2 == 1:
        print("is_odd")
    else:
        print("is_even")


isthis_odd = lambda x: True if x % 2 == 1 else False

isthis_odd(3)

is_odd(3)

a = 1


def vartest(a):
    a = a + 1
    print(a)


vartest(a)
print(a)

add = lambda c, b: c + b

result = add(3, 4)
print(result)
