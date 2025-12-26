# Python 学习笔记
笔记和测试代码印上传到了github，连接：https://github.com/WenxuanWu123/python-learning-notes.git
**强制推送方法：**
```
1. 执行upload.bat文件，在Powershell中输入:**
cd "python learning"; .\upload.bat
2. 直接在终端里边输入：cd "d:\coding-personal\python learning"; if(!(Test-Path .git)){git init *>$null; git remote add origin https://github.com/WenxuanWu123/python-learning-notes.git *>$null}; git add -A *>$null; git commit -m "更新内容" --allow-empty *>$null; git push -f origin main *>$null; Write-Host "上传完成！"
```
**12\26**
## 用markdown格式写作
1. 在TRAE中安装了markdown all in one 插件，预览方式为`Ctrl+Shift+V`
2. markdown格式中，用于象征python交互的>>>容易被理解为嵌套的引用（blockquote），因此在python交互中，需要用```符号来表示代码
```python
line1
line2
```
来表示python代码块。


## 学python
参考网址：[Python 学习笔记](https://www.liaoxuefeng.com/wiki/1016959663602400)。
### 数据类型与变量
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

### 列表(List)
列表是Python中最基本的数据结构之一，它是一个有序的集合，可以随时添加和删除其中的元素。

#### 创建列表
```python
# 地震台站列表
stations = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen']
print(stations)

# 地震震级列表
magnitudes = [3.2, 4.5, 6.1, 2.8, 5.3]
print(magnitudes)
```

#### 访问列表元素
```python
# 索引从0开始
stations = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen']
print(stations[0])  # 输出: Beijing
stations = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen']
print(stations[-1]) # 输出: Shenzhen (最后一个元素)

# 列表切片
print(stations[1:3])  # 输出: ['Shanghai', 'Guangzhou']
print(stations[:2])   # 输出: ['Beijing', 'Shanghai']
```

#### 列表常用方法
```python
# 添加元素
stations.append('Xian')

# 在指定位置插入元素
stations.insert(2, 'Hangzhou')

# 删除元素
removed_station = stations.pop()  # 删除最后一个元素
stations.remove('Shanghai')       # 删除指定元素

# 获取列表长度
print(len(stations))

# 检查元素是否存在
print('Beijing' in stations)  # 输出: True
```

### for循环
for循环是Python中最重要的控制结构之一，用于重复执行一段代码。

#### 基本语法
```python
# 遍历列表元素
for station in stations:
    print(f"处理台站: {station}")

# 通过索引遍历
for i in range(len(stations)):
    print(f"台站 {i+1}: {stations[i]}")

# 同时获取索引和值
for index, station in enumerate(stations):
    print(f"索引 {index}: 台站 {station}")
```

#### 循环控制
```python
# break - 退出循环
for magnitude in magnitudes:
    if magnitude > 5.0:
        print(f"发现强震: {magnitude}")
        break

# continue - 跳过当前迭代
for magnitude in magnitudes:
    if magnitude < 3.0:
        continue
    print(f"处理震级: {magnitude}")
```

#### 列表推导式
列表推导式是Python的高级特性，可以用简洁的语法创建列表。
```python
# 传统方式
strong_earthquakes = []
for magnitude in magnitudes:
    if magnitude >= 5.0:
        strong_earthquakes.append(magnitude)

# 列表推导式方式
strong_earthquakes = [magnitude for magnitude in magnitudes if magnitude >= 5.0]
```

#### 嵌套循环
```python
station_networks = [
    ['Beijing', 'Tianjin', 'Shijiazhuang'],  # 华北网络
    ['Shanghai', 'Nanjing', 'Hangzhou'],     # 华东网络
    ['Guangzhou', 'Shenzhen', 'Zhuhai']       # 华南网络
]

for network in station_networks:
    for station in network:
        print(f"台站: {station}")
```

#### 实际应用：地震数据处理
```python
# 地震事件数据
earthquake_events = [
    {'date': '2023-12-20', 'location': 'Beijing', 'magnitude': 3.2, 'depth': 10.5},
    {'date': '2023-12-21', 'location': 'Shanghai', 'magnitude': 4.5, 'depth': 15.2},
    {'date': '2023-12-22', 'location': 'Guangzhou', 'magnitude': 6.1, 'depth': 8.7}
]

# 筛选强震事件
strong_earthquakes = []
for event in earthquake_events:
    if event['magnitude'] >= 5.0:
        strong_earthquakes.append(event)

# 统计分析
total_magnitude = sum(event['magnitude'] for event in earthquake_events)
average_magnitude = total_magnitude / len(earthquake_events)
```