f = open("new.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("new.txt", 'r')
lines = f.read()
print(lines)
f.close()
