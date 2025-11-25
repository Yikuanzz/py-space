# Python 高级特性

## 第一课：生成器（Generator）与 `yield`

生成器函数用 `yield`，每次调用 `next()` 时 “暂停” 并返回一个值，下次从暂停处继续。

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# 使用
gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # 抛出 StopIteration
```

## 第二课：装饰器（Decorator）

装饰器是一种特殊的函数，它接收另一个函数作为参数，并返回一个新的函数，允许在不修改原函数的情况下，动态地增加功能。

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

## 第三课：上下文管理器（Context Maanger）与 `with` 语句

上下文管理器是一种协议（protocol），用于在进入和退出某个代码块时自动执行设置和清理操作。常见的用途是文件操作、数据库连接、锁机制等资源管理。

```python
from contextlib import contextmanager

@contextmanager
def managed_file(filename):
    print(f"Opening file: {filename}")
    f = open(filename, "w")
    try:
        yield f     # yield 返回的值就是 as 后的变量
    finally:
        print(f"Closing file: {filename}")
        f.close()

with managed_file("test.txt") as f: 
    f.write("Hello, world!")
```

## 第四课：迭代器协议与自定义迭代器（Iterator Protocol）

Python 的 `for` 循环、`list()`、`sum()` 等函数都依赖于迭代协议。这个协议由两个关键部分组成：
1、可迭代对象 `__iter__()`：返回一个迭代器对象。
2、迭代器：`__iter__() + __new__()`：实现逐个返回元素，直到抛出 `StopIteration` 异常。

```python
class Iterable:
    def __init__(self, stop):
        self.stop = stop
    def __iter__(self):
        return

class Interator:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

r = Range(2)
print(list(r))
print(list(r))
```

## 第五课：描述符（Decriptors）与属性管理

描述符是一个实现了描述符协议的对象，至少定义以下方法：

- `__get__(self, obj, objtype=None)`
- `__set__(self, obj, value)`
- `__delete__(self, obj)`

当一个类属性是描述符时，访问该属性会自动触发描述符的方法，而不是直接返回值。

```python
class ReadOnlyDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, obj, objtype=None):
        print(f"Accessing read-only attribute: {self.value}")
        return self.value


class MyClass:
    x = ReadOnlyDescriptor(42)
```

## 第六课：元类（Metaclass）基础

元类是创建类的“类”。换句话说，类本身也是对象，而这些对象由元类创建，默认情况下，Python 用 `type` 作为所有类的元类。

一般情况下，以下情况考虑用元类：

- 自动化代码生成：比如自动注册。
- 跨多个类共享行为：比如很多类都需要执行相同类型的设置或检查。
- 框架开发：比如 Django ORM 用元类来处理模型。

```python
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        ''' __new__ 是再类创建时调用 '''
        print(f"Creating class: {name}")
        # 执行逻辑 ...
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        ''' __init__ 是在类初始化的时候调用 '''
        print(f"Initializing class: {name}")
        super().__init__(name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass
```

## 第七课：异步编程入门（async/await）

异步编程允许编写非阻塞代码，尤其适合 IO 密集型操作。

- 异步编程：适合 IO 密集型操作，要理解事件循环；
- 多线程：适合 CPU 密集型和 IO 密集型，需要处理锁等同步机制；
- 多进程：适合 CPU 密集型，需要考虑进程间通信。

```python
async def task(name, seconds):
    print(f"Task {name} starting...")
    await asyncio.sleep(seconds)
    print(f"Task {name} finished.")

async def main():
    await asyncio.gather(
        task("Task 1", 1),
        task("Task 2", 2),
        task("Task 3", 3),
    )
```

## 第八课：类型提示进阶（Type Hints + Generics + Protocol）

类型提示用来提升代码的可读性，并且可以帮助静态检查器进行类型检查。

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

age: int = 25

print(greet("John"))
```
