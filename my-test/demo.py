import queue
import random
import threading
import time

p_sum, s_sum = 0, 0


def product(q: queue.Queue, q1: queue.Queue):
    while True:
        item = random.randint(1, 10000)
        q.put(item)
        q1.put(1)
        # print(threading.currentThread().getName() + "生产了" + str(item))


def consume(q: queue.Queue, q1: queue.Queue):
    while True:
        q.get()
        q1.put(1)
        # print(threading.currentThread().getName() + "消费了" + str(item))


def s_product(q: queue.Queue):
    global p_sum
    while True:
        p_sum += q.get()


def s_consume(q: queue.Queue, q1: queue.Queue, tasks: int):
    global s_sum
    while True:
        s_sum += q.get()
        if s_sum == tasks:
            q1.put(1)
            return


def summary():
    last_p_sum, last_s_sum = 0, 0
    t = time.time() + 1
    while True:
        local_time = time.time()
        if local_time >= t:
            t = local_time + 1
            print("生产效率(个/s): %.2f, 消费效率(个/s): %.2f ; 总生产: %d, 总消费: %d" % (
                p_sum - last_p_sum, s_sum - last_s_sum, p_sum, s_sum))
            last_p_sum, last_s_sum = p_sum, s_sum


if __name__ == '__main__':
    chan1 = queue.Queue(maxsize=200)
    chan2 = queue.Queue(maxsize=10)
    chan3 = queue.Queue(maxsize=10)
    end_chan = queue.Queue(maxsize=1)

    t_count = 500
    # t_tasks = random.choice([1000, 10000, 100000, 1000000, 10000000])
    t_tasks = 10000
    print("任务数: ", t_tasks)

    threading.Thread(target=summary, args=(), name="summary_thread", daemon=True).start()
    threading.Thread(target=s_product, args=(chan2,), name="s_product_thread", daemon=True).start()
    threading.Thread(target=s_consume, args=(chan3, end_chan, t_tasks), name="s_consume_thread", daemon=True).start()

    for val in range(t_count):
        threading.Thread(target=product, args=(chan1, chan2), name="product" + str(val), daemon=True).start()
        threading.Thread(target=consume, args=(chan1, chan3), name="consume" + str(val), daemon=True).start()

    end_chan.get()
    print("程序结束!!!", s_sum)
