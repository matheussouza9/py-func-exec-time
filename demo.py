from time import sleep
from functools import reduce

from py_func_exec_time import get_exec_time_timeit


def sum_while(n=1_000_000):
    acc = 0
    i = 0

    while i < n:
        acc += i
        i += 1

    return acc


def sum_for(n=1_000_000):
    acc = 0
    for i in range(n):
        acc += i

    return acc


def main():
    print("sum_while:", get_exec_time_timeit(sum_while))
    print("sum_for:", get_exec_time_timeit(sum_for))
    print("sum:", get_exec_time_timeit(sum, range(1_000_000)))
    print("reduce:", get_exec_time_timeit(reduce, lambda x, y: x+y, range(1_000_000)))
    print("sleep 1.1s:", get_exec_time_timeit(sleep, 1.1))


if __name__ == '__main__':
    main()