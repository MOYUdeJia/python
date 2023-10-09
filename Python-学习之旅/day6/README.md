# 函数和模块的使用
## 函数的作用
解决重复代码的问题。

## 定义函数
关键字*def*定义函数。函数名后的括号里放参数，函数执行完成后需要关键字*return*返回一个值.定义函数要有冒号。
```Python
def fac(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result
```

## 函数的参数
函数参数的使用规则：在定义函数时，括号内可以只写参数，也可以给参数默认值。  
在使用函数时，括号内可以什么都没有，此时函数若有参数则为默认值；当有多个参数时，可以只输入某一个参数；可以不按顺序输入参数值，但要表明参数。
```Python
from random import randint

def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c
# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))
```
当有多个参数时，具体几个参数由调用者决定，使用可变参数。
```Python
# 在参数名前面的*表示args是一个可变参数
def add(*args):
    toral = 0
    for val in args:
        total+=val
    return total

# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
```
## 用模块管理函数
目的：解决同一个.py文件里命名冲突的问题。  
解决方法：一个.py文件就是一个模块(moudle),在使用时，通过*import*关键字导入指定的模块来区分。

`module1.py`

```Python
def foo():
    print('hello, world!')
```

`module2.py`

```Python
def foo():
    print('goodbye, world!')
```

`test.py`

```Python
from module1 import foo

# 输出hello, world!
foo()

from module2 import foo

# 输出goodbye, world!
foo()
```
也可使用如下所示的方式区分使用哪一个`foo`函数。
`test.py`

```Python
import module1 as m1
import module2 as m2

m1.foo()
m2.foo()
```
如果导入的模块除了定义函数外还有其他可执行的代码，那么Python解释器在导入这个模块时就会执行这些代码，事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中，这样的话除非直接运行该模块，if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是&quot;\_\_main\_\_&quot;。
`module3.py`

```Python
def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
```

`test.py`

```Python
import module3

# 导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__
```
## 变量域的作用域
```Python
def foo():
    b = 'hello'
    def bar():# Python中可以在函数内部再定义函数
        c = True
        print(a)
        print(b)
        print(c)
    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    foo()
```
`if`分支中定义了一个变量`a`，这是一个全局变量（global variable），属于全局作用域，因为它没有定义在任何一个函数中。

`foo`函数中我们定义了变量`b`，这是一个定义在函数中的局部变量（local variable），属于局部作用域，在`foo`函数的外部并不能访问到它；但对于`foo`函数内部的`bar`函数来说，变量`b`属于嵌套作用域，在`bar`函数中我们是可以访问到它的。

`bar`函数中的变量`c`属于局部作用域，在`bar`函数之外是无法访问的。

事实上，Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索，我们之前用过的`input`、`print`、`int`等都属于内置作用域。

当函数外定义一个变量a，函数内在定义一个变量a，函数调用时优先选用函数内的变量a且不会影响函数外的变量a。

可以在函数中用`global a`来让a成为全局变量，会影响函数外的a。

在实际开发中，我们应该尽量减少对全局变量的使用。说了那么多，其实结论很简单，从现在开始我们可以将Python代码按照下面的格式进行书写，这一点点的改进其实就是在我们理解了函数和作用域的基础上跨出的巨大的一步。
```Python
def main():
    # Todo: Add your code here
    pass
if __name__ == '__main__':
    main()
```

