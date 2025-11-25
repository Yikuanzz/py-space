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

class Registry(type):
    registry = []

    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        if name != 'Base':      # 避免注册基类自身
            cls.registry.append(new_cls)
        return new_cls
    

class Base(metaclass=Registry):
    pass

class A(Base):
    pass

class B(Base):
    pass

class C(B):
    pass

print(Registry.registry)

class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        # 自动为每个字段生成 getter 和 setter 方法  
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, (int, str, float)): # 简化判断
                fields[key] = value
            
        for field, default in fields.items():
            attrs[f"get_{field}"] = lambda self, f = field: getattr(self, f)
            attrs[f"set_{field}"] = lambda self, value, f=field: setattr(self, f, value)

        attrs['_fields'] = fields
        return super().__new__(cls, name, bases, attrs)

class Model(metaclass=ModelMeta):
    pass

class Person(Model):
    id = 1
    name = "John"
    age = 20

p = Person()
print(p.get_id())
p.set_name("Jane")
print(p.get_name())


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    pass

a = SingletonClass()
b = SingletonClass()
assert a is b  # True

print(SingletonClass.__mro__)  