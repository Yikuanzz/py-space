from typing import TypeVar, List, Generic, Protocol, Callable, Optional

def greet(name: str) -> str:
    return f"Hello, {name}!"

age: int = 25

print(greet("John"))



T = TypeVar('T')

def first(items: List[T]) -> T:
    return items[0]

names: List[str] = ["John", "Jane", "Jim"]
print(first(names))

class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []
    
    def push(self, item: T):
        self.items.append(item)
    
    def pop(self) -> T:
        return self.items.pop()

# Shoot low aim high
int_stack = Stack[int]()
int_stack.push(1)
x = int_stack.pop()

# Structural Subtyping
# 鸭子类型原则：“如果它走起来像鸭子，叫起来像鸭子，那它就是鸭子。”
# 静态类型检查器默认使用名义子类型（必须显式继承）。
class Closeable(Protocol):
    def close(self) -> None: ...

def safe_close(obj: Closeable) -> None:
    obj.close()

class FileLike:
    def close(self) -> None:
        print("File closed")

class SocketLike:
    def close(self) -> None:
        print("Socket closed")

# 对两个类 进行检查
safe_close(FileLike())
safe_close(SocketLike())

class Drawable(Protocol):
    color: str
    def draw(self) -> None: ...

def render(itme: Drawable) -> None:
    print(f"Drawing {itme.color}")
    itme.draw()

class Circle:
    def __init__(self, color: str):
        self.color = color
    def draw(self) -> None:
        print(".Circle.")

render(Circle("red"))

def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

add = lambda a, b: a + b
result = apply(add, 1, 2)

def parse_id(user_id: int | str) -> str:
    return str(user_id)

class User:
    def __init__(self, id: int, name: str):
        self.id: int = id
        self.name: str = name

def find_user(name: str) -> User | None:
    if name == "John":
        return User(id=1, name="John")
    return None

user = find_user("Johnz")
if user is not None:
    print(user.id)
    print(user.name)
else:
    print("User not found")

K = TypeVar('K')
V = TypeVar('V')

class Cache(Generic[K, V]):
    def __init__(self) -> None:
        self._storage: dict[K, V] = {}
    
    def get(self, key: K) -> V | None:
        return self._storage.get(key)

    def set(self, key: K, value: V) -> None:
        self._storage[key] = value

# 使用
cache = Cache[str, int]()
cache.set("count", 42)
x = cache.get("count")  # x: int | None
if x is not None:
    print(x)
else:
    print("Cache miss")
