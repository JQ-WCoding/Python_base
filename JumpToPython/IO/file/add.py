f = open("new.txt", 'a')
for i in range(11, 20):
    data = "%d 번째 줄\n" % i
    f.write(data)
f.close()

