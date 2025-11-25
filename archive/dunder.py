# 1、对象的创建与销毁
class Example:
    def __new__(cls, *args, **kwargs):
        ''' 控制实例创建过程 '''
        print("Creating instance")
        return super().__new__(cls)

    def __init__(self, value):
        ''' 初始化实例属性 '''
        self.value = value
        print(f"Initializing with {value}")
    
    def __del__(self):
        ''' 对象销毁时会调用 '''
        print("Deleting instance")

# 2、表示与调试
class Example2:
    def __repr__(self):
        ''' 在调用类时返回 '''
        return f"{self.__class__.__name__}"
    
    def __str__(self):
        ''' 作为字符串返回时会进行调用 '''
        return "String Return Value"

# 3、比较操作
class Example3:
    def __init__(self):
        self.value = 0

    def __eq__(self, other):
        if not isinstance(other, Example3):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other):
        if not isinstance(other, Example):
            return NotImplemented
        return self.value < other.value

# 4、算数运算符
# __sub__, __mul__, __truediv__, __floordiv__ 
class Example4:
    def __init__(self):
        self.value = 0

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Example(self.value + other)
        elif isinstance(other, Example):
            return Example(self.value + other.value)
        else:
            return NotImplemented

    def __iadd__(self, other): # 对应 +=
        if isinstance(other, (int, float)):
            self.value += other
            return self
        else:
            return NotImplemented

# 5、容器相关
class Exmaple5:
    def __init__(self):
        self.items = []

    def __len__(self):
        ''' 返回容器长度 '''
        return len(self.items)

    def __getitem__(self, index):
        ''' 返回指定索引的元素  obj[key]'''
        return self.items[index]

    def __setitem__(self, index, value):
        ''' 设置指定索引的元素  obj[key] = value '''
        self.items[index] = value
    def __delitem__(self, index):
        ''' 删除指定索引的元素  del obj[key] '''
        del self.items[index]


# 6、迭代器相关
class Example6:
    def __iter__(self):
        ''' 返回迭代器 '''
        return iter(self.items)

    def __next__(self):
        ''' 返回下一个元素 '''
        return next(self.items)

# 7、上下文管理器
class Example7:
    def __enter__(self):
        ''' 进入上下文管理器 '''
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        ''' 退出上下文管理器 '''
        return self

# 8、调用行为
class Example8:
    def __call__(self, *args, **kwargs):
        ''' 使实例可以像函数一样被调用 '''
        return "Called"

# 通过魔法方法实现 OrderedSet 有序集合
class OrderedSet:
    def __init__(self, iterable=None):
        self.items = []
        self.set_items = set()
        if iterable is not None:
            for item in iterable:
                self.add(item)

    def add(self, item):
        if item not in self.set_items:
            self.items.append(item)
            self.set_items.add(item)

    def discard(self, item):
        if item in self.set_items:
            self.items.remove(item)
            self.set_items.discard(item)

    def __contains__(self, item):
        return item in self.set_items

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __str__(self):
        return "{" + ", ".join(map(str, self.items)) + "}"

    def __repr__(self):
        return f"OrderedSet({self.items})"

oset = OrderedSet([1, 2, 3])
print(oset)  # OrderedSet([1, 2, 3])

oset.add(4)
print(oset)  # OrderedSet([1, 2, 3, 4])

oset.add(3)  # 不添加重复元素
print(oset)  # OrderedSet([1, 2, 3, 4])

for item in oset:
    print(item)
# 输出 1, 2, 3, 4

print(len(oset))  # 4
print(3 in oset)  # True