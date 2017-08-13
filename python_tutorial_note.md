## [python tutorial](http://python.usyiyi.cn/translate/python_278/tutorial/index.html) 学习笔记##

+  [1.引言](http://python.usyiyi.cn/translate/python_278/tutorial/appetite.html)
 + Python允许您将您的程序拆分成可以在其它Python程序中重复使用的模块。它拥有大量的标准模块，你可以将其用作你的程序的基础 — 或者作为学习Python编程的示例。这些模块提供诸如文件I/O、系统调用、套接字和甚至用户图形界面接口，例如GTk。 **（我会试着尽量标准化编程，模块，复用）**  
 - Python是可扩展的：一旦你真的着迷，你可以把Python解释器链接到C编写的应用程序中，并把它当作那个程序的扩展或命令行语言。**（将解释器链接到程序中是什么感觉）**
+  [2.解释器](http://python.usyiyi.cn/documents/python_278/tutorial/interpreter.html)
 +  一个增强的*交互式解释器*是IPython，它已经存在相当一段时间，具有tab补全、 对象exploration 和高级的历史记录功能。它也可以彻底定制并嵌入到其他应用程序中。另一个类似的增强的交互式环境是bpython。**（我需要一个交互式的解释器吗？，可以提供什么好处 ,比如：[ipython](http://ipython.org/)）**
 +  **交互模式下**：这种模式下解释器以初始提示符提示下一个命令，主提示符通常为三个大于号（>>>）；对于续行解释器以从提示符提示，默认为三个点（...）。
 +  2.2.3. 源程序的编码：在Python源文件中可以使用非ASCII编码。最好的方法是在#!行的后面再增加一行特殊的注释来定义源文件的编码：\# -\*- coding: encoding-*-
通过此声明，源文件中的所有字符将被视为由encoding编码，并且可以直接写指定编码方式的Unicode字符串常量。在Python库参考手册的codecs小节中，可以找到所有可能的编码方式列表。 
+  [3.python简介](http://python.usyiyi.cn/translate/python_278/tutorial/introduction.html)
