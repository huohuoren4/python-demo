import multiprocessing, queue, random, threading, time


# 生产者消费者模式
def product(q: queue.Queue, gl: dict):
    while True:
        item = random.randint(1, 10000)
        q.put(item)
        with gl["s_lock"]:
            gl["p_sum"] += 1  # 大概计数
        # time.sleep(0.02)
        # print(threading.currentThread().getName() + "生产了" + str(item))


def consume(q: queue.Queue, tasks: int, gl: dict):
    while True:
        q.get()
        with gl["s_lock"]:
            if gl["s_sum"] == tasks:
                if not gl["S_STOP"].is_set():
                    gl["S_STOP"].set()
                    print(threading.current_thread().getName() + "s_sum=%d" % gl["s_sum"])
                return
            gl["s_sum"] += 1
        time.sleep(0.02)
        # print(threading.currentThread().getName() + "消费了" + str(item))


def summary(q: queue.Queue, p_name: str, gl: dict):
    last_p_sum, last_s_sum = 0, 0
    t = time.time() + 1
    while True:
        local_time = time.time()
        if local_time >= t:
            t = local_time + 1
            t_format = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(local_time))
            p_sum01 = gl["p_sum"]
            s_sum01 = gl["s_sum"]
            print(
                t_format + "\t进程名:" + p_name + "\t生产效率(个/s): %.2f, 消费效率(个/s): %.2f ; 总生产: %d, 总消费: %d, 通道中的线程数: %s, 活跃线程数: %d"
                % (p_sum01 - last_p_sum, s_sum01 - last_s_sum, p_sum01, s_sum01, q.qsize(), threading.active_count()))
            last_p_sum, last_s_sum = p_sum01, s_sum01


def run(p_name: str):
    # 线程数
    g_val = {
        "p_sum": 0,
        "s_sum": 0,
        "s_lock": threading.BoundedSemaphore(value=5),
        "S_STOP": threading.Event()
    }
    t_count = 100
    chan1 = queue.Queue(maxsize=int(t_count * 0.5))
    chan1.full()
    # 任务数
    t_tasks = 10000000
    print("任务数: %d" % t_tasks)
    start_t = time.time()
    threading.Thread(target=summary, args=(chan1, p_name, g_val), name="summary_thread", daemon=True).start()
    for val in range(t_count):
        threading.Thread(target=product, args=(chan1, g_val), name="product" + str(val), daemon=True).start()
        threading.Thread(target=consume, args=(chan1, t_tasks, g_val), name="consume" + str(val), daemon=True).start()

    while not g_val["S_STOP"].is_set():
        pass
    total_t = time.time() - start_t
    print("程序结束!!! 进程名:%s s_sum=%d, 总消费效率: %.2f, 总耗时: %.3f" % (
        p_name, g_val["s_sum"], g_val["s_sum"] / total_t, total_t))


if __name__ == '__main__':
    # 多进程多线程实现
    for val in range(2):
        name = "p" + str(val)
        p1 = multiprocessing.Process(target=run, args=(name,), name=name)
        p1.start()
