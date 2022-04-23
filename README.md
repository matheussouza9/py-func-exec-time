# py-func-exec-time
A very simple function to measure the execution time of your functions and return a human readable string

## Usage example
```python
from py_func_exec_time import get_exec_time_timeit


def awesome_func(*args **kwargs):
    ...


print(get_exec_time_timeit(awesome_func, *args, **kwargs))
```

```
00h 00m 00s 25ms
```

You can see a few more examples in `demo.py`

# Requirements
Python 3.5+