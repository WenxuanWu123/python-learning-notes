# Python 学习笔记
**12\26**
## 用markdown格式写作
在TRAE中安装了markdown all in one 插件，预览方式为`Ctrl+Shift+V`
## 学python
参考网址：[Python 学习笔记](https://www.liaoxuefeng.com/wiki/1016959663602400)。
整数、浮点数、字符串。
整数运算永远是精确的（除法也是精确的），而浮点数运算则可能会有四舍五入的误差。
转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\，例子如下：
    1. print('I\'m ok.')
    2. print('I\'m learning\nPython.')
    3. print('\\\n\\') #这个\本身前边也需要转义，因此就有\\的结构

Python还允许用r''表示''内部的字符串默认不转义，例子如下：
print(r'I\'m OK') #这时候可以和上边的对比，发现问题

Python允许用'''...'''的格式表示多行内容，例子如下：
print('''line1
line2
line3 ''')

在多行符号''' '''之前加入r，可以让后边的转义符无用
print(r'''hello,\n
world''')
