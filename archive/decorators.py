import time
from datetime import datetime

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_hello_twice():
    print("Hello!")


def do_twice_with_return(func):
    def wrapper_do_twice(*args, **kwargs):
        first_result = func(*args, **kwargs)
        second_result = func(*args, **kwargs)
        return first_result, second_result
    return wrapper_do_twice

@do_twice_with_return
def say_hello_twice_with_return(name):
    return f"Hello {name}"


def repeat(num_times):
    def decorator_repeat(func):
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper_repeat
    return decorator_repeat

@repeat(num_times=3)
def say_hello_three_times(name):
    print(f"Hello {name}")


def log_execution(show_time=False):
    def decorator_log(func):
        def wrapper_log(*args, **kwargs):
            start_time = datetime.now()
            print(f"[{start_time}] Function '{func.__name__}' started.")
            result = func(*args, **kwargs)
            end_time = datetime.now()
            if show_time:
                elapsed_time = (end_time - start_time).total_seconds()
                print(f"[{end_time}] Function '{func.__name__}' finished in {elapsed_time:.2f} seconds.")
            else:
                print(f"[{end_time}] Function '{func.__name__}' finished.")
            return result
        return wrapper_log
    return decorator_log

@log_execution(show_time=True)      # return decorato_log
def simulate_work(duration: int):   # return wrapper_log
    print("Doing work...")
    time.sleep(duration)


if __name__ == "__main__":
   simulate_work(3)         # call wrapper_log(3)