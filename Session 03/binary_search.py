import random
from time import clock

import matplotlib.pyplot as plt
from tqdm import tqdm


def binary_search(array: dict, target: int):
    left, right = 0, len(array) - 1

    if len(array) == 0:
        return False

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return True

        elif array[mid] < target:
            left = mid + 1

        elif array[mid] > target:
            right = mid - 1

    return False


def search(array, target):
    """simple search in an array for target

    :param array: input array to search in
    :param target: target number to search for in array
    :return: boolean indicating target is in array
    """
    for num in array:
        if num == target:
            return True

    return False


if __name__ == "__main__":

    binary_search_time = []
    simple_search_time = []

    max_array_length = 1000
    max_random_number = 2 * max_array_length

    for i in tqdm(range(max_array_length)):
        array = list(range(i))
        random_numbers = random.sample(range(0, max_random_number), 1000)

        # binary search
        t1 = clock()
        for num in random_numbers:
            binary_search(array, num)
        t2 = clock()
        binary_search_time.append(t2-t1)

        # simple search
        t1 = clock()
        for num in random_numbers:
            search(array, num)
        t2 = clock()
        simple_search_time.append(t2-t1)

    # plot
    plt.plot(range(max_array_length), binary_search_time)
    plt.plot(range(max_array_length), simple_search_time)
    # plt.xscale("log")
    plt.show()
