###"笨办法"学python练习题

**ex4.py**

+ **变量（ variable）**用来指代某个东西的名字。 

**ex5.py** 

1. print"round()"如何实现print中的函数调用。
2. 可以编制文本菜单将单位提前选择，当然需要if then 语句。
3. ？格式化字符串=字符串+%+tuple(数组)
4. **格式化字符（format string）**

__ex8.py__

*  p29页:_有`%r`python会用最有效的方式打印出字符串，而不是完全按照你写的方式打印。_(__那么我如何知道自己输出是什么样的？__)
*  `%r`是用来调试的，我想知道怎么用？r被称作**“原始表示”（raw representation）**


**ex9.py**
 
+ **总结：**print 后有`,`则不换行，继续显示。print 中有`\n`则新行 

**ex10.py**

+ p34页的代码需要**重新看下。** 
+ **转义字符（escape sequences）** 

**ex11.py**

+ 引入**raw_input()**函数

**ex12.py**

+  语句python -m是python以脚本方式运行模块。
+  **pydoc**是文档生成工具。 [pydoc用法](http://www.jb51.net/article/67119.htm)
例如	`D:\>python -m pydoc -p 1234 #比如说: 端口为1234`
	`pydoc server ready at http://localhost:1234/`
	`pydoc server stopped`

**ex13.py**

+ **import语句：** 可以将python的**模块（module）**(某种特性)引入脚本。
+ **参数变量（argument variable）:**这个变量保存着你运行python脚本时传递给python脚本的参数。（执行命令就应该输入的。）
+ **解包（unpack）:**将所有的参数依次赋值给左边的变量。

**ex14.py**

+ p43我也不知道为什么python必须在命令行中运行，而不能在python环境中运行。
 
**ex15.py**
  
+ **“单下划线” 开始的成员变量叫做保护变量**，意思是只有类对象和子类对象自己能访问到这些变量；
+ **"双下划线"开始的是私有成员** ，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。
+ 在python解释器中运行open,read。需要这样做`txt = open(filename)`→`print txt.read()`
+ `txt = open(filename)`返回的是文件对象，而非文件内容，所以，想知道内容还需要	`txt.read()`,我觉得还应该及时的`txt.close()` 
+ **from sys import argv** sys是个软件包，这句话的意思是从软件包中取出argv这个特性来，供我使用。 

**ex16.py**

+ 会在**当前（powershell运行程序的目录）**目录下**生成（即使不存在参数文件也产生）**文件
+ 文件操作的命令**汇总**
  + close 关闭文件
  + read 读取文件
  + readline 读取文件中一行
  + truncate 清空文件
  + write(stuff) 将stuff写入文件
+ **为什么不设计个程序把所有前面编写的文件汇总起来？**

**ex17.py**

+  关于open 模式：
  + w     以写方式打开，
  + a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
  + r+     以读写模式打开
  + w+     以读写模式打开 (参见 w )
  + a+     以读写模式打开 (参见 a )
  + rb     以二进制读模式打开
  + wb     以二进制写模式打开 (参见 w )
  + ab     以二进制追加模式打开 (参见 a )
  + rb+    以二进制读写模式打开 (参见 r+ )
  + wb+    以二进制读写模式打开 (参见 w+ )
  + ab+    以二进制读写模式打开 (参见 a+ )
+ "w"（write）写入模式，"r"（read）表示读取，"a"（append）表示追加。
+ "+"修饰符，这样的话文件将以同时读写的方式打开。
+ **如果只写open（filename）那就使用"r"模式打开，这是open（）函数的默认工作方式。**
+ **常见的文件运算：** 
  + 操作                     解释
  + output=open('/tmp/python.data','w') 创建输出文件，写入文件
  + input=open('/tmp/python.data','r') 创建输入文件，读取文件
  + input=open('/tmp/python.data')   创建输入文件，读取文件 r是默认值
  + aString=input.read()         把整个文件读进一个字符串
  + aString=input.read(N)         读取前面的N个字节到一个字符串
  + aString=input.readline(N)      读取下一行到一个字符串
  + aList=input.readlines()         读取剩下的行到一个字符串列表
  + output.write(aString)         写入字节字符串到文件
  + output.writelines(aList)    把列表内所有字符串写入到文件,列表里不能有数字，数字需要转换为字符串
  + output.close()            手动关闭（当文件收集完成时会关闭文件
  + output.flush()            把输出缓冲区刷到硬盘中，但不关闭文件。
  + anyfile.seek(N)            修改文件位置到偏移量N处以便进行一下操作

**ex18.py**
 
+ **使用#1和#2，它们可以让你创建“迷你脚本”或者“小命令”**

+ **函数定义**以def开始，函数名以字符和下划线组成数字不能出现在首位，函数名紧跟括号，可以不要参数，多个参数需要用“，”隔开，参数名不能重复，函数括号后有冒号，定义代码前有四个空格（1个Tab）,结束时取消缩进。
+ *args中的的星号是将所有参数都接受进来，然后放到args的列表中。

**ex19.py**

+ 有10种不同的方式运行函数（理论上有无穷多种方式运行一个函数，有趣！）

**ex20.py**  
 
+ file.seek()可以将文件游标移动到文件的任意位置,file.seek()方法标准格式是：seek(offset,whence=0),offset：开始偏移量，也就是代表需要移动偏移的字节数。 whence：给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
 
