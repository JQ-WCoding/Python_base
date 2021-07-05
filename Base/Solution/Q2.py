# Q1
a = 80
b = 75
c = 55
print((a + b + c) / 3)


# Q2
def checkNum(num):
    if num % 2 == 1:
        return "odd"
    else:
        return "even"


print(checkNum(13))

pin = "881120-1068234"


# Q3
def str(num):
    print(num[0:6])
    print(num[7:14])


str(pin)

# Q4
print(pin[7:8])

# Q5
a = "a:b:c:d"
a = a.replace(':', '#')
print(a)

# Q6
b = [1, 3, 5, 4, 2]
print(b)
print(sorted(b))
print(sorted(b, reverse=True))

# Q7
c = ['Life', 'is', 'too', 'short']
print(" ".join(c))

# Q8
d = (1, 2, 3)
d += (4,)
print(d)

# Q10
a = {'A': 90, 'B': 80, 'C': 70}
print(a.pop('B'))

# Q11
a = [1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5]
print(set(a))
