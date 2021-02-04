import threading
import requests
import time
urls = ["https://www.baidu.com/","https://www.baidu.com/","https://www.baidu.com/","https://www.baidu.com/",
        "https://www.baidu.com/","https://www.baidu.com/","https://www.baidu.com/","https://www.baidu.com/",
        "https://www.baidu.com/","https://www.baidu.com/"]

def worker():
    while True:
        try:
            url = urls.pop()
        except IndexError:
            break  # Done.

        requests.get(url)
for j in range(10):
    t0 = time.time()
    threads = []
    for _ in range(j):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    t1 = time.time()
    print(j,"threads:",t1-t0)

