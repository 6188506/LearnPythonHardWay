[Sublime笔记](https://www.w3cschool.cn/sublimetext/)
------------
+ **[Sublime Text编辑](https://www.w3cschool.cn/sublimetext/vgj4cozt.html)**
 
  + **多重选择** `Ctrl + D` 光标所在词高亮，再次`Ctrl + D`选择下一个词。如果需要跳过`Ctrl + K`后`Ctrl + D`,要回退用`Ctrl + U`
  + 如何调用sublime的**全程指导**？
  + 同时编辑多个区域,`Ctrl + Shift + L`将当前选中区域打散。
  + `Ctrl + J`可以吧当前选中区域合并为一行。

 
+ **[Sublime Text查找&替换](https://www.w3cschool.cn/sublimetext/pxlwqozt.html)**

  + 快速查找：多重编辑`Ctrl + D` + 跳下/上一个位置 `F3/Shift+F3` (ALT+F3选中所有位置)
  + 标准查找：`CTRL+F`标准查找+`Alt+Enter`所有位置 (Search in selection功能使           局部重命名非常方便。)
             `CTRL+H` 标准替换，
  + 正则表达式查找&替换：[精通正则表达式](https://book.douban.com/subject/2154713/);  [正则表达式30分钟入门教程](https://deerchao.net/tutorials/regex/regex-1.htm);  [MSDN正则表达式教程.aspx](https://msdn.microsoft.com/zh-cn/library/d9eze55x(v=vs.90).aspx);  以及在线测试工具（regexpal和regexer）;[正则表达式30分钟入门教程](http://www.oschina.net/question/12_9507)
  + 多文件查找 :`Ctrl + Shift + F`多文件搜索和替换（和搜狗热键冲突）

+ **[Sublime Text跳转](https://www.w3cschool.cn/sublimetext/r34xkozt.html)**

  +  <font color=red>`Ctrl + P`</font>文件跳转
  +  对于**Markdown**，`Ctrl + R`会列出其大纲，非常实用。
  +  `Ctrl + G`+行号：跳转到指定行
  +  **组合跳转** `Ctrl + P` 匹配文件后(在sublime中被称为"go to any way") ①@（符号跳转） ②#keyword（关键字跳转） ③：行号（行号跳转）
  
+  [Sublime Text窗口&标签](https://www.w3cschool.cn/sublimetext/iogsbozt.html)

  + **标签：**<font color=red>`Ctrl + N`</font>新标签
            <font color=red>`Ctrl + W`</font>关标签
  + **分屏：**<font color=red>`Alt + Shift + 2`</font>左右分屏
            <font color=red>`Alt + Shift + 8`</font>上下分屏
            <font color=red>`Alt + Shift + 5`</font>四分屏
  + **全屏：** <font color=red>`F11`</font>普通全屏
              <font color=red>`Shift + F11`</font>勿扰全屏

+ [Sublime Text风格](https://www.w3cschool.cn/sublimetext/tvwinozt.html)
  
   + 可以找sublime主题尝试？？？ 

+  [Sublime Text编码](https://www.w3cschool.cn/sublimetext/uotmiozt.html)

   +  **手动格式化**<font color=red>`Ctrl + [`</font>左缩进
               <font color=red>`Ctrl + ]`</font>右缩进
               <font color=red>`Ctrl + Shift + V`</font>可以以当前缩进粘贴代码（非常实用,暂时还没用它）
   + **智能格式化（插件）**
      + HTMLBeautify：格式化HTML。
      + AutoPEP8：格式化Python代码。
      + Alignment：进行智能对齐。
   + **自动完成** 用Tab自动补全
   + **括号** 
      + **<font color=red>`Ctrl + M`</font> 快速在起始、结尾括号间切换。
      + **<font color=red>`Ctrl + +Shift + M`</font>快速选择括号间的内容。
      + **<font color=red>`Ctrl + +Shift + J`</font>对于缩进型语言（python）可以用，不好用，跨行的括号选内容和尾巴括号，还需要研究下？
      + **BracketHighlighter插件**以高亮显示配对括号以及当前光标所在区域
    + **命令行：**Sublime​REPL？是插件吗？
+  [Sublime Text快捷键列表](https://www.w3cschool.cn/sublimetext/qkv6bozt.html)

+ **通用（General）**
 - ↑↓←→：上下左右移动光标，注意不是不是KJHL！
 - Alt：调出菜单
 - Ctrl + Shift + P：调出命令板（Command Palette）
 - Ctrl + `：调出控制台

+ **编辑（Editing）**
  - Ctrl + Enter：在当前行下面新增一行然后跳至该行
 - Ctrl + Shift + Enter：在当前行上面增加一行并跳至该行
 - Ctrl + ←/→：进行逐词移动
 - Ctrl + Shift + ←/→进行逐词选择
 - Ctrl + ↑/↓移动当前显示区域
 - Ctrl + Shift + ↑/↓移动当前行
 
+ **选择（Selecting）**
 - Ctrl + D：选择当前光标所在的词并高亮该词所有出现的位置，再次Ctrl + D选择该词出现的下一个位置，在多重选词的过程中，使用Ctrl + K进行跳过，使用Ctrl + U进行回退，使用Esc退出多重编辑
 - Ctrl + Shift + L：将当前选中区域打散
 - Ctrl + J：把当前选中区域合并为一行
 - Ctrl + M：在起始括号和结尾括号间切换
 - Ctrl + Shift + M：快速选择括号间的内容
 - <font color=red>`Ctrl + Shift + J`：快速选择同缩进的内容</font>：
 - <font color=red>`Ctrl + Shift + Space`：快速选择当前作用域（Scope）的内容</font>

+ **查找&替换（Finding&Replacing）**
 - F3：跳至当前关键字下一个位置
 - Shift + F3：跳到当前关键字上一个位置
 - Alt + F3：选中当前关键字出现的所有位置
 - Ctrl + F/H：进行标准查找/替换，之后：
 - Alt + C：切换大小写敏感（Case-sensitive）模式
 - Alt + W：切换整字匹配（Whole matching）模式
 - Alt + R：切换正则匹配（Regex matching）模式
 - Ctrl + Shift + H：替换当前关键字
 - Ctrl + Alt + Enter：替换所有关键字匹配
 - Ctrl + Shift + F：多文件搜索&替换

+ **跳转（Jumping）**
 - Ctrl + P：跳转到指定文件，输入文件名后可以：
 - @ 符号跳转：输入@symbol跳转到symbol符号所在的位置**（类名，函数名）**
 - 关键字跳转：输入#keyword跳转到keyword所在的位置
 - : 行号跳转：输入:12跳转到文件的第12行。
 - Ctrl + R：跳转到指定符号
 - Ctrl + G：跳转到指定行号
 
+ **窗口（Window）**

 - Ctrl + Shift + N：创建一个新窗口
 - Ctrl + N：在当前窗口创建一个新标签
 - Ctrl + W：关闭当前标签，当窗口内没有标签时会关闭该窗口
 - Ctrl + Shift + T：恢复刚刚关闭的标签
+ **屏幕（Screen）**
 - F11：切换普通全屏
 - Shift + F11：切换无干扰全屏
 - Alt + Shift + 2：进行左右分屏
 - Alt + Shift + 8：进行上下分屏
 - Alt + Shift + 5：进行上下左右分屏分屏之后，使用Ctrl + 数字键跳转到指定屏，使用Ctrl + Shift + 数字键将当前屏移动到指定屏