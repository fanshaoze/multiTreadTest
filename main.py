import threading
import time
def multi_threading_test(count):
	for i in range(count):
		t = i / 3
if __name__ == '__main__':
	count = 100000000
	thread_num = 1
	threads = []
	time_0 = time.time()
	for i in range(thread_num):
		t_0 = threading.Thread(target=multi_threading_test, args=(count,))
		t_0.start()
		threads.append(t_0)
	for t in threads:
		t.join()
	time_1 = time.time()
	print(time_1 - time_0)
