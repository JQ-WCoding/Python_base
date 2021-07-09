import threading
import time


def long_task():
    for j in range(5):
        time.sleep(1)  # 1초 대기
        print("working:%s\n" % j)


print("Start")

threads = []

for i in range(5):
    t = threading.Thread(target=long_task)  # 스레드 생성
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()  # join 으로 스레드가 종료될때까지 기다린다

print("End")
