# Python 学习笔记
笔记和测试代码印上传到了github，连接：https://github.com/WenxuanWu123/python-learning-notes.git
强制推送方法：
```
1. # 进入你的项目目录
cd "d:\coding-personal\python learning"

# 强制添加所有文件（包括已修改的）
git add -A

# 强制提交（覆盖历史记录）
git commit -m "更新学习笔记和代码"

# 强制推送到 GitHub（覆盖远程内容）
git push -f origin main
2. 直接在终端里边输入：cd "d:\coding-personal\python learning"; if(!(Test-Path .git)){git init *>$null; git remote add origin https://github.com/WenxuanWu123/python-learning-notes.git *>$null}; git add -A *>$null; git commit -m "更新内容" *>$null; git push -f origin main *>$null
```
**12\26**
## 用markdown格式写作
1. 在TRAE中安装了markdown all in one 插件，预览方式为`Ctrl+Shift+V`
2. markdown格式中，用于象征python交互的>>>容易被理解为嵌套的引用（blockquote），因此在python交互中，需要用
```python
line1
line2
```
来表示python代码块。


## 学python
参考网址：[Python 学习笔记](https://www.liaoxuefeng.com/wiki/1016959663602400)。
整数、浮点数、字符串。
整数运算永远是精确的（除法也是精确的），而浮点数运算则可能会有四舍五入的误差。
转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\，例子如下：
```python
    1. print('I\'m ok.')
    2. print('I\'m learning\nPython.')
    3. print('\\\n\\') #这个\本身前边也需要转义，因此就有\\的结构
```

Python还允许用r''表示''内部的字符串默认不转义，例子如下：
print(r'I\'m OK') #这时候可以和上边的对比，发现问题

Python允许用'''...'''的格式表示多行内容，例子如下：
print('''line1
line2
line3 ''')

在多行符号''' '''之前加入r，可以让后边的转义符无用
```python
print(r'''hello,\n
world''')
```

布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来：
```python
>>> True
True
>>> False
False
>>> 3 > 2
True
>>> 3 > 5
False
```