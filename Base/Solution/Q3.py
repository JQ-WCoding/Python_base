# Q1
a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

# Q2
i = 1
result = 0
while i < 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)

# Q3
i = 1
while i < 6:
    print('*' * i)
    i += 1

# Q4
for i in range(1, 101):
    print(i)

# Q5
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
result = 0
for i in a:
    result += i

result = result / len(a)
print(result)

# Q6
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)

print(result)

result = [n * 2 for n in numbers]
print(result)
