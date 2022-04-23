from timeit import default_timer as timer, timeit
from typing import Callable


def get_exec_time_perf_counter(func: Callable, *func_args, **func_kwargs) -> str:
    '''
    using time.perf_counter, which is more flexible to use, but not so accurate as timeit.timeit
    '''

    start = timer()
    try:
        func(*func_args, **func_kwargs)
    finally:
        end = timer()

    elapsed = end - start
    return human_readable_elapsed_time(elapsed)


def get_exec_time_timeit(func: Callable, *func_args, **func_kwargs) -> str:
    '''
    using timeit.timeit, that make some optimizations and is more accurate.
    '''
    elapsed = timeit(lambda: func(*func_args, **func_kwargs), number=1)
    return human_readable_elapsed_time(elapsed)


def human_readable_elapsed_time(elapsed: float) -> str:
    '''
    returns elapsed time formatted for a human easily read
    '''
    if elapsed < 0:
        raise Exception('elapsed time must not be negative')

    elif elapsed == 0:
        return '0ms'

    hours, minutes_remainder = divmod(elapsed, 3600)
    minutes, seconds = divmod(minutes_remainder, 60)
    milliseconds = round((seconds % 1) * 1000)

    return f"{f'{int(hours):02d}h'} {f'{int(minutes):02d}m'} {f'{int(seconds):02d}s'} {f'{milliseconds:02d}ms'}"

