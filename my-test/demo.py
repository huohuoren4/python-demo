import random
import time
from typing import Generator

# yield实现的生产者消费者模式
def product():
    for _ in range(1000000):
        item = random.randint(1, 100)
        print("生产了", item)
        c = yield item  # 类似于单向通道
        print("消耗了", c)


def consume(g: Generator):
    # 启动生产器
    # 或者: item = g.next()
    item = g.send(None)
    while True:
        try:
            item = g.send(item)
        except StopIteration:
            return

if __name__ == '__main__':
    start = time.time()
    consume(product())
    print("总耗时: ", time.time() - start)