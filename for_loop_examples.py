# Python for循环学习
# 在地震数据处理中的应用示例

# 1. 基本for循环
print("=== 基本for循环 ===")
stations = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Chengdu']
print("遍历所有台站:")
for station in stations:
    print(f"正在处理台站: {station}")

# 2. 通过索引遍历
print("\n=== 通过索引遍历 ===")
magnitudes = [3.2, 4.5, 6.1, 2.8, 5.3]
print("地震震级信息:")
for i in range(len(magnitudes)):
    print(f"地震 {i+1}: 震级 {magnitudes[i]}")

# 3. 使用enumerate同时获取索引和值
print("\n=== 使用enumerate ===")
earthquake_dates = ['2023-12-20', '2023-12-21', '2023-12-22', '2023-12-23', '2023-12-24']
print("地震日期信息:")
for index, date in enumerate(earthquake_dates):
    print(f"序号 {index+1}: 日期 {date}")

# 4. 循环中的条件判断
print("\n=== 循环中的条件判断 ===")
print("检测强震事件(震级>=5.0):")
for magnitude in magnitudes:
    if magnitude >= 5.0:
        print(f"强震警告! 震级: {magnitude}")
    else:
        print(f"正常地震. 震级: {magnitude}")

# 5. 嵌套循环
print("\n=== 嵌套循环 ===")
station_networks = [
    ['Beijing', 'Tianjin', 'Shijiazhuang'],  # 华北网络
    ['Shanghai', 'Nanjing', 'Hangzhou'],     # 华东网络
    ['Guangzhou', 'Shenzhen', 'Zhuhai']       # 华南网络
]

network_names = ['华北网络', '华东网络', '华南网络']

for network_idx, network in enumerate(station_networks):
    print(f"\n{network_names[network_idx]}:")
    for station in network:
        print(f"  - {station}")

# 6. 循环控制语句
print("\n=== 循环控制语句 ===")
print("查找第一个震级大于4.0的地震:")
for i, magnitude in enumerate(magnitudes):
    if magnitude > 4.0:
        print(f"找到! 地震 {i+1}, 震级 {magnitude}")
        break  # 找到后立即退出循环

print("\n跳过震级小于3.0的地震:")
for magnitude in magnitudes:
    if magnitude < 3.0:
        continue  # 跳过当前迭代
    print(f"处理震级: {magnitude}")

# 7. 列表推导式 - Python的高级特性
print("\n=== 列表推导式 ===")
# 传统方式
strong_earthquakes = []
for magnitude in magnitudes:
    if magnitude >= 5.0:
        strong_earthquakes.append(magnitude)
print(f"传统方式获取强震列表: {strong_earthquakes}")

# 列表推导式方式
strong_earthquakes_comp = [magnitude for magnitude in magnitudes if magnitude >= 5.0]
print(f"列表推导式获取强震列表: {strong_earthquakes_comp}")

# 8. 实际地震数据处理示例
print("\n=== 实际地震数据处理示例 ===")
# 模拟地震波形数据点
waveform_data = [0.1, 0.2, 0.15, 0.3, 0.8, 1.2, 1.5, 1.3, 0.9, 0.4, 0.2, 0.1]
threshold = 1.0  # 触发阈值

print("分析地震波形数据:")
for i, amplitude in enumerate(waveform_data):
    if amplitude > threshold:
        print(f"时间点 {i}: 振幅 {amplitude} - 检测到信号!")
    elif amplitude > 0.5:
        print(f"时间点 {i}: 振幅 {amplitude} - 弱信号")
    else:
        print(f"时间点 {i}: 振幅 {amplitude} - 背景噪声")

# 9. 循环中的累加计算
print("\n=== 循环中的累加计算 ===")
total_energy = 0
for magnitude in magnitudes:
    # 简化的能量计算 (实际公式更复杂)
    energy = 10 ** (1.5 * magnitude)
    total_energy += energy
    print(f"震级 {magnitude}: 能量 {energy:.2e}")

print(f"总地震能量: {total_energy:.2e}")

# 10. zip函数 - 同时遍历多个列表
print("\n=== 使用zip同时遍历多个列表 ===")
locations = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Chengdu']
magnitudes = [3.2, 4.5, 6.1, 2.8, 5.3]
dates = ['2023-12-20', '2023-12-21', '2023-12-22', '2023-12-23', '2023-12-24']

print("地震事件汇总:")
for location, magnitude, date in zip(locations, magnitudes, dates):
    print(f"日期: {date}, 地点: {location}, 震级: {magnitude}")