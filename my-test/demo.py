import multiprocessing
import random
import time
from concurrent.futures import ProcessPoolExecutor, Future


def task():
    time.sleep(random.randint(1, 10))
    print(multiprocessing.current_process().name, "执行结束")
    return 0


def done(fu: Future):
    print(multiprocessing.current_process().name, fu.result())


if __name__ == '__main__':
    pool = ProcessPoolExecutor()
    for i in range(2):
        f = pool.submit(task)
        f.add_done_callback(fn=done)
    pool.shutdown()
    print("主进程")
