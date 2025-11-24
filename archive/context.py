import time
from contextlib import contextmanager

class ManagedFile:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        # __enter__(self): 进入 with 块时调用
        # 返回复制给 as 后的变量
        print(f"Opeing file: {self.filename}") 
        self.file = open(self.filename, "w")
        return self.file    

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # __exit__(self, exc_type, exc_value, exc_traceback): 退出 with 块时调用
        # 处理异常
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
        if exc_type is not None:
            print(f"Exception occurred: {exc_value}")
        return False


@contextmanager
def managed_file(filename):
    print(f"Opeing file: {filename}")
    f = open(filename, "w")
    try:
        yield f
    finally:
        print(f"Closing file: {filename}")
        f.close()


@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Elapsed time: {end - start} seconds")

@contextmanager
def suppress_exception(exception_type):
    try:
        yield
    except exception_type:
        pass    # 忽略指定异常


if __name__ == "__main__":
    # with ManagedFile("data.txt") as file:
    #     file.write("Hello, World!")
    #     # file.write(123)

    # with managed_file("data.txt") as file:
    #     file.write("Hello, World! from contextmanager")
    #     #file.write(123)

    # with timer():
    #     time.sleep(2)
    #     sum(i for i in range(1000000))

    # with suppress_exception(ValueError):
    #     print(10 / 0)