# Python 第一次打卡

> 这是阿里云天池龙珠训练营第一次打卡的笔记内容

[TOC]



### 基础知识

1. 注释：#(单个)  ''' '''(多个)快捷键：Ctrl+/ (多行注释)

2. 运算符号：

   `^`按位异或符号 `**`乘方符号 `//`整除符号 `/`正常除符号

   `in` `not in`判断包含性

   `is` `not is`判断相同性

   三元判断符：

   `N = A if 条件 else B #如果满足条件则N = A，否则为B`

   ```python
   def Min(x,y):
       small = x if x < y else y
       return small
   
   print(Min(7,9))
   
   #7
   ```


   位运算的某些使用可以加速运算

   ：一个数对另外一个数进行两次异或对于该数本身，利用该性质可以快速交换两个整数：

   ```python
   a,b = map(int,input().split())
   a ^= b;
   b ^= a;
   a ^= b;
   print(a,b)
   \#1 2 -> 2 1
   ```

3. input 函数使用

   [input()函数使用详解](https://blog.csdn.net/qq_46018836/article/details/105199040?ops_request_misc=%7B%22request%5Fid%22%3A%22163386252716780262594166%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=163386252716780262594166&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-105199040.pc_search_result_control_group&utm_term=python+input函数&spm=1018.2226.3001.4187)

   input() 返回类型为字符串类型，一般使用时加类型转换关键词如：`int(input())`

   1. 返回参数字符串类型

      ```python
      a = input()b = input()print(a+b)
      
      #\#1 2 -> 12
      ```

   2. 变量插入input函数

      input将直接打印所输入的字符串，因此在input内插入变量要注意①变量一定为字符串形式，最好在前面加上`str()`关键词②变量与字符串之间通过`'+'`符号连接而不是`','`

      ```python
      a = 'python'
      b = input(str(a) + '请输入license')
      #a为字符串类型，用字符串连接符'+',不能使用 input(str(a),'请输入license'),','为分割字符串和变量的符号
      print(b)
      
      #python请输入license123 -> 123
      ```

   3. 多输入型input函数（split()函数）

      ```python
      a,b = input('请输入a,b的值：').split()
      print(a,b)
      
      #1 2 -> 1 2
      a,b = input('请输入a,b的值：').split(',')
      print(a,b)
      
      #1,2 -> 1 2
      ```

      split()函数返回值为一个列表，因此转换类型时不能单使用转换关键词，需要加上map传递给列表中的所有值

   4. 多输入型input函数（类型转换）

      ```python
      a,b = map(int,input('请输入a,b的值：').split())
      print(a,b)
      print(type(a),type(b))
      
      #请输入a,b的值：1 21 2<class 'int'> <class 'int'>
      ```

4. print()函数

   [print()函数详解](https://blog.csdn.net/sinat_28576553/article/details/81154912?ops_request_misc=&request_id=&biz_id=102&utm_term=python%20print&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-81154912.nonecase&spm=1018.2226.3001.4187)

   1. 数据格式化输出的格式和注意事项
   2. 转换标志的含义
   3. 取消自动换行的方法

5. 函数

   [Python函数详解](https://blog.csdn.net/weixin_45393094/article/details/105264311?ops_request_misc=%7B%22request%5Fid%22%3A%22163387102416780264060519%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=163387102416780264060519&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-105264311.pc_search_result_control_group&utm_term=python函数&spm=1018.2226.3001.4187)

6. 断言语句

   断言语句格式：`assert 条件` 当条件为False时，程序崩溃`AssertionError`，可在程序检查中使用
   循环语句

   ```python
   assert 3>7
   
   #AssertionError
   ```

7. range()函数

   函数格式：`range([start,] stop[, step=1])`

8. enumerate()函数（枚举函数）`enumerate(sequence, [start=0])`：

   > sequence: 一个序列、迭代器或其他支持迭代对象
   >
   > start：下标起始位置。

   返回 enumerate(枚举) 对象enumerate()与 for 循环的结合使用。

   ```python
   elements = ['1','2','3']
   print(list(enumerate(elements,1)))
   for i,element in enumerate(elements,1):
       print(i,element,end = ',')
   
   #[(1, '1'), (2, '2'), (3, '3')]
   #1 1,2 2,3 3
   ```

   用 enumerate(A) 不仅返回了 A 中的元素，还顺便给该元素一个索引值 (默认从 0 开始)。此外，用 enumerate(A, j) 还可以确定索引起始值为 j。

   ```python
   for i,element in enumerate(elements,3):
       print(i,element,end = ',')
       
   #3 1,4 2,5 3
   ```

9. 推导式

   结构：`[ expr for value in collection [if condition] ]`  

10. 异常检测与处理
    1. try - except 语句，若检测出现异常并且与except异常原因一致则跳过try语句剩余部分直接进入except语句，再执行之后的代码。

> Exception 主要有
>
> - OverflowError：数值运算超出最大限制
> - ZeroDivisionError：除数为零
> - AssertionError：断言语句（assert）失败
> - AttributeError：尝试访问未知的对象属性  
> - OSError：操作系统产生的异常（例如打开一个不存在的文件 ）
> - ImportError：导入模块失败的时候  
> - IndexError：索引超出序列的范围
> - KeyError：字典中查找一个不存在的关键字
> - MemoryError：内存溢出（可通过删除对象释放内存）
> - NameError：尝试访问一个不存在的变量  
> - SyntaxError：语法错误导致的异常  
> - TypeError：不同类型间的无效操作
> - ValueError：传入无效的参数  

```python
try:
检测范围
except Exception[as reason]:
出现异常后的处理代码
```

一个 try 语句可能包含多个 except 子句，分别来处理不同的特定的异常。最多只有一个分支会被执行 。**在运用时应注意不同异常的从属关系，坚持对其规范排序，从最针对性的异常到最通用的异常**。

```python
'''键错误应该在查询错误之前'''
dict1 = {'a': 1, 'b': 2, 'v': 22}
try:
    x = dict1['y']
except KeyError:
    print('键错误')
except LookupError:
    print('查询错误')
else:
    print(x)
    
#键错误
```

 	2. try-except-finally语句 finally语句最后一定执行
 	3. try-except-else语句 else语句只在程序无异常时执行

### 关于Python

1. 关于python文件之间的相互关系以及文件的入口参数含义：

   [Python入口函数](https://blog.csdn.net/Iron_Ye/article/details/80044242?ops_request_misc=%7B%22request%5Fid%22%3A%22163387300916780274144200%22%2C%22scm%22%3A%2220140713.130102334.pc%5Fall.%22%7D&request_id=163387300916780274144200&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-3-80044242.pc_search_result_control_group&utm_term=python+函数入口参数为列表&spm=1018.2226.3001.4187)

   对于python，每一个文件相当于一个模块，模块间的引用通过`import()`函数，函数调用通过（文件名.函数名）来访问，每个模块都有一个 `__name__` 属性，当其值是 `__main__` 时，表明该模块自身在运行，否则是被其他文件引入。

2. 调试步骤

   [调试步骤详解](https://blog.csdn.net/qq_33472146/article/details/90606359?ops_request_misc=%7B%22request%5Fid%22%3A%22163403948816780261918467%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=163403948816780261918467&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-90606359.pc_search_result_control_group&utm_term=Pycharm+debug&spm=1018.2226.3001.4187)



