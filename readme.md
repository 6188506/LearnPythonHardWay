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

+ 会在**当前（powershell运行程序的目录）**目录下**产生（即使不存在参数文件也产生）**文件
+ 文件操作的命令**汇总**
+ **为什么不设计个程序把所有前面编写的文件汇总起来？**