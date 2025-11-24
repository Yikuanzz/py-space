class ReadOnlyDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, obj, objtype=None):
        print(f"Accessing read-only attribute: {self.value}")
        return self.value


class MyClass:
    x = ReadOnlyDescriptor(42)

class NonNegativeInteger:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"Attribute {self.name} must be a non-negative integer")
        obj.__dict__[self.name] = value

class Person:
    age = NonNegativeInteger("age")
    height = NonNegativeInteger("height")


# Lazzy Property
class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = self.func(obj)
        setattr(obj, self.name, value)      # 替换自身为普通属性
        return value 

class HeavyComputation:
    @LazyProperty
    def expensive_value(self):
        print("Computing expensive value...")
        return sum(i*i for i in range(1000000))

    def foo(self):
        pass

class TypedAttribute:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __delete__(self, obj):
        del obj.__dict__[self.name]

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise ValueError(f"Attribute {self.name} must be a {self.expected_type}")
        obj.__dict__[self.name] = value

class Student:
    name = TypedAttribute("name", str)
    score = TypedAttribute("score", int)


if __name__ == "__main__":
    print(HeavyComputation.__dict__)
    print("--------------------------------\n")
    h = HeavyComputation()
    print(h.expensive_value)
    print(h.expensive_value)

    print("--------------------------------\n")
    print(h.__dict__)

    print("--------------------------------\n")
    s = Student()
    s.name = "John"
    s.score = 100
    print(s.name)
    print(s.score)