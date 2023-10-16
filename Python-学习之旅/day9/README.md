## 面向对象进阶

### @property装饰器
考虑使用@property包装器来包装getter（访问器）方法和setter（修改器）方法，使得对属性的访问既安全又方便，代码如下所示。

**@property**需要用在要包装的函数前，表示getter修改器。@property装饰器用于将一个方法转换为属性，使得该方法可以像访问属性一样被调用，而不需要使用括号进行调用。@property装饰器定义的属性是只读的，不能直接对其进行赋值。用一次写一次，后面没有冒号


**@函数名.setter**表示setter修改器。用一次写一次，后面没有冒号
```Python
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 修改器 - getter方法
    @property
    def name(self):
        return self._name

    # 修改器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋' % self._name)
        else:
            print(f'{self._name}正在玩LOL')


def main():
    person = Person('北鸟', 15)
    person.play()
    person.age = 22
    person.play()
    print(person.name) # 通过@property使得name的调用不再需要括号


if __name__ == '__main__':
    main()
```

### __slots__魔法
__slots__可限定自定义类型的对象只能绑定某些属性。需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。

>意思是你通过__slots__限定一些属性后就不能在这个类外给其他属性赋值了。
```Python
class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)



person = Person('王大锤', 22)
person.play()
person._gender = '男'  #没问题,只能修改__slots__里有的。
print(person._gender)
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True
```
### 静态方法和类方法
我们在类中定义的方法都是对象方法，也就是说这些方法都是发送给对象的消息。例如我们传入三角形的三条边计算三角形的面积和周长，但我不并不知道这三条边能不能构成三角形，因此需要先判断，而判断的方法是属于类的，而不是对象的。以使用**静态方法**来解决这类问题，代码如下所示。
```Python
from math import sqrt

class Triangle(object):

    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a,b,c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        p = self.perimeter()/2
        return sqrt(p*(p-self._a)*(p-self._b)*(p-self._c))

def main():
    a,b,c=3,4,5
    if Triangle.is_valid(a,b,c):
        t=Triangle(a,b,c)
        print(f'周长是{t.perimeter()}')
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(f'面积是{t.area()}')
        # print(Triangle.area(t))
    else:
        print('无法构成三角形')


if __name__ == '__main__':
    main()
```
和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象，代码如下所示。
```Python
from time import time, localtime, sleep

class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
```
类方法可以通过类本身或类的实例进行调用，它们通常用于执行与类相关的操作或对类属性进行操作。

在类方法内部，可以访问类的属性。
### 类之间的关系
简单的说，类和类之间的关系有三种：is-a、has-a和use-a关系。

- is-a关系也叫继承或泛化，比如学生和人的关系、手机和电子产品的关系都属于继承关系。
- has-a关系通常称之为关联，比如部门和员工的关系，汽车和引擎的关系都属于关联关系；关联关系如果是整体和部分的关联，那么我们称之为聚合关系；如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），那么这种就是最强的关联关系，我们称之为合成关系。
- use-a关系通常称之为依赖，比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系。
![](./res/uml-example.png)

### 继承和多态
刚才我们提到了，可以在已有类的基础上创建新类，这其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，从而减少重复代码的编写。提供继承信息的我们称之为父类，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或衍生类。子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力，在实际开发中，我们经常会用子类对象去替换掉一个父类对象，这是面向对象编程中一个常见的行为，对应的原则称之为里氏替换原则。下面我们先看一个继承的例子。
>summary:子类可继承父类的属性和方法，还可以定义特有的。
```Python
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋' % self._name)
        else:
            print(f'{self._name}正在玩LOL')

class Student(Person):

    def __init__(self,name,age,grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,grade):
        self._grade = grade

    def study(self,course):
        print(f'{self._grade}分的{self._name}正在学习{course}')

class Teacher(Person):

    def __init__(self,name,age,title):
        super().__init__(name,age)
        self._title = title

    @property
    def title(self):
        return (self._title)

    @title.setter
    def title(self,title):
        self._title = title

    def teach(self,course):
        print(f'{self.name}正在讲{course}')


def main():
    stu = Student('蒂朵',18,98)
    print(stu.grade)
    stu.grade = 99
    print(stu.grade)
    stu.study('数学')

    tea = Teacher('枫眠',24,'英语')
    tea.title = 'Python'
    print(tea.title)
    tea.teach('英语')


if __name__ == '__main__':
    main()
```
子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。

通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，当我们调用这个经过子类重写的方法时，不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）。
```Python
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
```
在上面的代码中，我们将`Pet`类处理成了一个抽象类，所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。Python从语法层面并没有像Java或C#那样提供对抽象类的支持，但是我们可以通过`abc`模块的`ABCMeta`元类和`abstractmethod`包装器来达到抽象类的效果，如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）。上面的代码中，`Dog`和`Cat`两个子类分别对`Pet`类中的`make_voice`抽象方法进行了重写并给出了不同的实现版本，当我们在`main`函数中调用该方法时，这个方法就表现出了多态行为（同样的方法做了不同的事情）。



