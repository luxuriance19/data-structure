# 使用函数装饰器实现单例
def singleton(kk): # 一般都是用cls来代替kk，我这里是为了让自己区分清楚Cls和kk。
    _instance = {}

    def inner():
        if kk not in _instance:
            _instance[kk] = kk()
        return _instance[kk]

    # python中返回函数的写法，不需要带（）
    return inner

@singleton
class Cls():
    def __init__(self):
        pass

cls1 = Cls()
cls2 = Cls()
print(cls1==cls2)

#==================================
'''
使用类装饰器实现单例
'''
class Singleton():
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}
    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]

@Singleton
class Cls2():
    def __init__(self):
        pass

cls1 = Cls2()
cls2 = Cls2()
print(cls1==cls2)


# 另外一种用法
class Cls3():
    pass

Cls3 = Singleton(Cls3) # 继承Cls3类
cls3 = Cls3()
cls4 = Cls3()
print(cls3==cls4)

"""
利用New， Metaclass关键字
metaclass可以通过__metaclass__ 创造类（class）， 类(class) 通过__new__创造实例
"""
# 使用__new__方法创造实例
class Single():
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls,*args,**kwargs)
        return cls._instance
    def __init__(self):
        pass

single1 = Single()
single2 = Single()
print(id(single1)) # id()返回对象的内存的地址
print(single1==single2)

'''
使用metaclass创建单例
'''
# type 创造类的方法
def func(self):
    print("do sth")

# type: class type(name, bases, dict), name：类名， bases：基类的元组， dict： 字典，类内定以的命名空间变量， 返回新的类型对象
# type()不会考虑子类是一种父类的类型，不考虑继承关系
# isinstance()考虑子类是一种父类类型，考虑继承关系

Klass = type("Klass", (), {"func":func})
c = Klass()
c.func()

class Singleton(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instance[cls]

class Cls4(metaclass=Singleton):
    pass
cls1 = Cls4()
cls2 = Cls4()
print(id(cls1)==id(cls2))