from time import clock

import matplotlib.pyplot as plt
from tqdm import tqdm


def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def cached_fib(n, memo):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    elif memo[n] > 0:
        return memo[n]

    memo[n] = cached_fib(n-1, memo) + cached_fib(n-2, memo)
    return memo[n]


if __name__ == "__main__":

    fib_time = []
    cached_fib_time = []

    max_array_length = 25

    for num in tqdm(range(max_array_length)):
        # fib(n)
        t1 = clock()
        fib(num)
        t2 = clock()
        fib_time.append(t2-t1)

        # cached fib(n)
        t1 = clock()
        memo = [0] * (num + 1)
        cached_fib(num, memo)
        t2 = clock()
        cached_fib_time.append(t2-t1)

    # plot
    plt.plot(range(max_array_length), fib_time, '-r')
    plt.plot(range(max_array_length), cached_fib_time, '-b')
    plt.savefig("plot.pdf")
    plt.show()
