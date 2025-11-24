class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

class Range2:
    def __init__(self, stop):
        self.stop = stop
    
    def __iter__(self):
        return Range2Interaor(self.stop)    # 每次新建一个迭代器

class Range2Interaor:
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

# 大多数情况下在 __iter__ 下用生成器就可以了
class FibonacciIterable:
    def __init__(self, max_count):
        self.max_count = max_count
    
    def __iter__(self):
        a, b = 0, 1
        count = 0
        while count < self.max_count:
            yield a
            a, b = b, a + b
            count += 1

class Reverser:
    def __init__(self, data):
        self.data =data
    
    def __iter__(self):
        index = len(self.data) - 1
        while index >= 0:
            yield self.data[index]
            index -= 1


if __name__ == "__main__":
    # countdown = Countdown(5)
    # for i in countdown:
    #     print(i)

    # r = Range2(3)
    # print(list(r))
    # print(list(r))

    # fib = FibonacciIterable(5)
    # for n in fib:
    #     print(n)
    
    # print(list(fib))       
    rev = Reverser([10, 20, 30])
    for x in rev:
        print(x)  # 应输出 30, 20, 10
    print(list(rev))  # [30, 20, 10]