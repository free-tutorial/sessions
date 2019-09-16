from tqdm import tqdm
from collections import deque
from time import clock
import matplotlib.pyplot as plt

queue_time = []
list_time = []
CALL_NUM = 10000

for size in tqdm(range(1, 10001)):

    queue_ = deque(list(range(size)))
    list_ = list(range(size))

    t1 = clock()
    for _ in range(CALL_NUM):
        queue_[size//2]
    t2 = clock()
    queue_time.append((t2-t1)/CALL_NUM)

    t1 = clock()
    for _ in range(CALL_NUM):
        list_[size//2]
    t2 = clock()
    list_time.append((t2-t1)/CALL_NUM)

plt.plot(range(10000), queue_time)
plt.plot(range(10000), list_time)
plt.show()