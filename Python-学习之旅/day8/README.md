## 面向对象编程基础

### 类和对象
类是对象的蓝图和模板，而对象是类的实例。类是抽象的概念，而对象是具体的东西。在面向对象编程的世界中，一切皆为对象，对象都有属性和行为，每个对象都是独一无二的，而且对象一定属于某个类（型）。当我们把一大堆拥有共同特征的对象的静态特征（属性）和动态特征（行为）都抽取出来后，就可以定义出一个叫做“类”的东西。

### 定义类
使用class关键字定义类,定义类的一行有冒号。
```Python
class student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self,name,age):  #def __init__():创建对象时初始化操作
        self.name = name
        self.age = age
        
    def study(self,course_name):
        print(fr'{self.name}正在学习{course_name}')
        
    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age<18:
            print('只能看熊出没')
        else:
            print('看你想看的')
```
> **说明：** 写在类中的函数，我们通常称之为（对象的）方法，这些方法就是对象可以接收的消息。
### 创建和使用对象
```Python
通过__init__()里的内容创建初始值
def main():
    stu1 = student('贝蕾亚',15)
    stu1.study('Python程序设计')

    stu2 = student('妮蔻',18)
    stu2.watch_movie()

    stu3 = student('易',30)
    stu3.watch_movie()

if __name__ == '__main__ ':
    main()
```
### 访问可见性问题（访问权限）
在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头，下面的代码可以验证这一点。
```Python
class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test.__foo)


if __name__ == "__main__":
    main()
```
Python并没有从语法上严格保证私有属性或方法的私密性，它只是给私有的属性和方法换了一个名字来妨碍对它们的访问，事实上如果你知道更换名字的规则仍然可以访问到它们，下面的代码就可以验证这一点。
```Python
class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()
```
在实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类无法访问（后面会讲到）。所以大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，本类之外的代码在访问这样的属性时应该要保持慎重。这种做法并不是语法上的规则，单下划线开头的属性和方法外界仍然是可以访问的，所以更多的时候它是一种暗示或隐喻。

### 面向对象的支柱
面向对象有三大支柱：封装、继承和多态。

封装："隐藏一切可以隐藏的实现细节，只向外界暴露（提供）简单的编程接口"。只需要给对象发送一个信息（调用方法）就可以执行方法中的代码，
