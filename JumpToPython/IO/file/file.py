f = open("new.txt", 'w')

for i in range(1, 11):
    data = "%d 번째 줄\n" % i
    f.write(data)

f.close()
