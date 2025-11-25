from operator import attrgetter, itemgetter
import operator
import itertools
from functools import lru_cache, partial, reduce, wraps
import time

# 排序字典列表
students = [
    {'name': 'Alice', 'score': 95},
    {'name': 'Bob', 'score': 87},
    {'name': 'Charlie', 'score': 92}
]

# 按照 Score 降序
sorted_students = sorted(students, key=itemgetter('score'), reverse=True)
print(sorted_students)

# 排序对象列表
class Person:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"

people = [Person("Alice", 23), Person("Bob", 30), Person("Charlie", 25)]
youngest = min(people, key=attrgetter('age'))
print(youngest)

# 1、无限迭代器
# count(start=0, step=1)
for i in itertools.count(10, 2): 
    if i > 20: break
    print(i)

# cycle(iterable)
# for c in itertools.cycle('AB'):
#     pass

# repeate(object, times=None)
res = list(itertools.repeat('A', 3))
print(res)

# 2、组合迭代器
# chain(*iterables) 拼接多个可迭代对象
res = list(itertools.chain([1, 2, 3], [4, 5, 6]))
print(res)

# compress(data, selectors) 根据选择器过滤数据
res = list(itertools.compress([1, 2, 3, 4, 5], [True, False, True, False, True]))
print(res)

# islice(iterable, start, stop, step=1) 切片
res = list(itertools.islice([1, 2, 3, 4, 5], 2, 4))
print(res)

# 3、排列组合
# permutations(iterable, r=None) —— 排列
res = list(itertools.permutations('ABC', 2))
print(res)
# [('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B')]

# combinations(iterable, r) —— 组合（无重复）
res = list(itertools.combinations('ABC', 2))
print(res)
# [('A','B'), ('A','C'), ('B','C')]

# product(*iterables, repeat=1) —— 笛卡尔积
res = list(itertools.product('AB', '12'))
print(res)
# [('A','1'), ('A','2'), ('B','1'), ('B','2')]


class Timer:
    def __init__(self):
        self.start_time = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        print(f"Time taken: {self.end_time - self.start_time} seconds")
# 1、自动缓存函数结果
@lru_cache(maxsize=128)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def fib_no_cache(n: int) -> int:
    if n < 2:
        return n
    return fib_no_cache(n-1) + fib_no_cache(n-2)

with Timer() as t:
    print(fib(20))

with Timer() as t:
    print(fib_no_cache(20))

# 2、固定部分参数

def power(base: int, exponent: int) -> int:
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(4))  # 16
print(cube(3))    # 27

# 3、累计计算
# 计算乘积
numbers = [1, 2, 3, 4]
product = reduce(operator.mul, numbers, 1)
print(product)

# 合并字典
dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
merged = reduce(lambda a, b: {**a, **b}, dicts, {'q': 0})
print(merged)
# {'q': 0, 'a': 1, 'b': 2, 'c': 3}

# 4、修复装饰器元数据
# 用 @wraps 可以保留原函数的 __name__ 和 __doc__ 信息

def my_decorator(func):
    @wraps(func)     # wraps 将原函数的元数据复制到了 wrapper 上                                                             
    def wrapper(*args, **kwargs):
        print("Before")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    ''' Say Hello '''
    print("Hello")
print(greet.__name__)
print(greet.__doc__)

# 前10个偶数的平方
evens = itertools.islice(itertools.count(0, 2), 10)
squares = map(lambda x: x*x, evens)
print(list(squares))

# 笛卡尔积
list1 = [1, 2, 3]
list2 = [4, 5]
pairs = itertools.product(list1, list2)
sums = map(lambda pair: operator.add(pair[0], pair[1]), pairs)
print(list(sums))