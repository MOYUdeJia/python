## 字符串和常用数据结构

### 使用字符串
所谓**字符串**，就是由零个或多个字符组成的有限序列，一般记为![$${\displaystyle s=a_{1}a_{2}\dots a_{n}(0\leq n \leq \infty)}$$](./res/formula_5.png)。在Python程序中，如果我们把单个或多个字符用单引号或者双引号包围起来，就可以表示一个字符串.
```Python
s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')
```

可以在字符串中使用`\`（反斜杠）来表示转义.
`\n`不是代表反斜杠和字符n，而是表示换行；而`\t`也不是代表反斜杠和字符t，而是表示制表符。表示'要写成\'，同理想表示\要写成\\.

在\后面还可以跟一个八进制或者十六进制数来表示字符，例如\141和\x61都代表小写字母a，前者是八进制的表示法，后者是十六进制的表示法。也可以在\后面跟Unicode字符编码来表示字符，例如\u9a86\u660a代表的是中文“骆昊”。
```Python
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)
# 输出：abcabc 骆昊
```

在字符串前加r'字符串'既可让**\**不转义
```Python
s1 = r'\'hello, world!\''
```
Python为字符串提供了非常丰富的运算符，我们可以使用`+`运算符来实现字符串的拼接，可以使用`*`运算符来重复一个字符串的内容，可以使用`in`和`not in`来判断一个字符串是否包含另外一个字符串（成员运算），我们也可以用`[]`和`[:]`运算符从字符串取出某个字符或某些字符（切片运算），代码如下所示。

```Python
s1 = 'hello ' * 3
print(s1) # hello hello hello 
s2 = 'world'
s1 += s2
print(s1) # hello hello hello world
print('ll' in s1) # True
print('good' in s1) # False
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2]) # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246
print(str2[::-1]) # 654321cba
print(str2[-3:-1]) # 45
```
还有其他对字符串的处理方法：
```Python
str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1)) # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or')) # 8
print(str1.find('shit')) # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # True
```

**字符串的格式化输出：**
```Python
a, b = 5, 10
print('%d * %d = %d' %(a,b,a*b))
```
```Python
a, b = 5, 10
print('{0} * {1} = {2}'.format(a,b,a*b))
```
```Python
a, b = 5, 10
print(f'{a} * {b} = {a*b}')
```
```Python
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
```
## 列表、元组、集合和字典

### 使用列表
列表长度，遍历列表
```Python
List1 = [1,3,5,4,100]
# 计算列表长度(元素个数)
print(len(list1)) # 5
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历列表元素
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)
```
添加移除元素
```Pytohn
list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)
list1.insert(1, 400)
# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1) # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(len(list1)) # 9
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
	list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1) # [1, 400, 5, 7, 100, 200, 1000, 2000]
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1) # [400, 5, 7, 100, 200, 1000]
# 清空列表元素
list1.clear()
print(list1) # []
```
也可进行切片操作：fruits4 = fruits[-3:-1]  区间前闭后开。从左边开始数序号从0开始，从右边开始数序号从-1开始。

字符串排序
```Python
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)  # 默认是按字母顺序
# sorted函数返回列表排序后的拷贝不会修改传入的列表
sorted
list3 = sorted(list1, reverse=True)  # 按字母逆序
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)    # 按字符串长度由小到大哦
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序，上面的都是产生新列表。
list1.sort(reverse=True)
print(list1)
```
### 生成式和生成器

我们还可以使用列表的生成式语法来创建列表，代码如下所示。

```Python
f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
print(f)
# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
print(f)
for val in f:
    print(val)
```

### 元组
元组用(),列表用[],数组用{}
```Python
# 定义元组
t = ('嘉辉', 38, True, '四川成都')
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])
# 遍历元组中的值
for member in t:
    print(member)
# 元组不能修改它的元素，可以先转换成列表list(),然后再转换成元组tuple()
t = ('王大锤', 20, True, '云南昆明')
print(t)
# 将元组转换成列表
person = list(t)
print(person)
# 列表是可以修改它的元素的
person[0] = '李小龙'
person[1] = 25
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
```
优点：元组内容不能被修改，更容易维护,创建时间和占用的空间上面都优于列表。如果不需要对元素进行添加、删除、修改的时候，可以考虑使用元组，当然如果一个方法要返回多个值，使用元组也是不错的选择。

### 集合
不能有重复的元素，允许交并补运算
```Python
# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)
```     
增加和删除元素
```Python
set1.add(4)
set1.add(5)
set2.update([11, 12])
set2.discard(5)  # 删除元素5，如果没有不会报错 比remove更安全。
if 4 in set2:
    set2.remove(4)
print(set1, set2) # {1,2,3,4,5,} {1，2，3，6，7，8，9，11，12}
print(set3.pop())   # 移除集合中最后一位元素，并返回这个元素的值。  1
print(set3) # {2.3}
```
```Python
# 集合的交集、并集、差集、对称差运算
print(set1 & set2) # 交集
# print(set1.intersection(set2))
print(set1 | set2) # 并集
# print(set1.union(set2))
print(set1 - set2) # 差集，从set1中减去set1和set2共有的元素。
# print(set1.difference(set2))
print(set1 ^ set2)  # 对称差集 ，set1和set2的并集减去交集
# print(set1.symmetric_difference(set2))

# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))
```
### 字典
字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开。
```Python

# 创建字典的字面量语法
scores = {'贝蕾亚': 95, '妮蔻': 78, '佐伊': 82}
print(scores) # {'贝蕾亚': 95, '妮蔻': 78, '佐伊': 82}
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3) # {'one': 1, 'two': 2, 'three': 3, 'four': 4} {'a': '1', 'b': '2', 'c': '3'} {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# 通过键可以获取字典中对应的值
print(scores['贝蕾亚']) # 95
print(scores['佐伊']) # 82
# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}') # 贝蕾亚: 95   妮蔻: 78     佐伊: 82
# 更新字典中的元素
scores['贝蕾亚'] = 65
scores['诸葛王朗'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores) # {'贝蕾亚': 65, '妮蔻': 78, '佐伊': 82, '诸葛王朗': 71, '冷面': 67, '方启鹤': 85}
if '武则天' in scores:
    print(scores['武则天'])  # None
print(scores.get('武则天'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60))
# 删除字典中的元素
print(scores.popitem()) # 删除最后一项
print(scores.popitem())
print(scores.pop('贝蕾亚', 100)) # 删除指定的某项
print(scores)
# 清空字典
scores.clear()
print(scores)
```

>**小结：** 只有元组是比较简单的，只有生成式()。字典也比较简单，但是形式特殊有键值对{}。列表[]和集合{}的创建可以用生成式或者生成器，有增删查改的操作。
>
> 列表list()、集合set()、字典dict（）都可以有生成式和生成器产生，元组只能生成式。