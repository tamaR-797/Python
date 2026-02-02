import time
import functools


def run_time_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        finish = time.perf_counter()
        timer = finish - start
        return timer, result
    return wrapper

def cache_decorator(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

def fib_no_cache(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


@cache_decorator
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


@run_time_decorator
def exc1():
    for i in range(1000000):
        i = i + 1

@run_time_decorator
def exc2():
    for i in range(1000):
        i = i * i



time_no_cache, result_no_cache = run_time_decorator(fib_no_cache)(100)
print(f"without cache took {time_no_cache}  result={result_no_cache}")


timer, result= run_time_decorator(fib)(100)
print(f" with cache took {timer} result={result}")




print("exc1 time:", exc1()[0])
print("exc2 time:", exc2()[0])
