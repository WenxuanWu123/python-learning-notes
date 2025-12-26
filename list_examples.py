# Python列表(List)基础学习
# 在地震数据处理中的应用示例

# 1. 创建列表
print("=== 创建列表 ===")
# 地震台站列表
stations = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Chengdu']
print(f"台站列表: {stations}")

# 地震震级列表
magnitudes = [3.2, 4.5, 6.1, 2.8, 5.3, 4.0]
print(f"震级列表: {magnitudes}")

# 混合类型数据
earthquake_info = ['2023-12-26', 'Guangdong', 3.2, True, 23.5]
print(f"地震信息: {earthquake_info}")

# 2. 访问列表元素
print("\n=== 访问列表元素 ===")
print(f"第一个台站: {stations[0]}")
print(f"第三个台站: {stations[2]}")
print(f"最后一个台站: {stations[-1]}")
print(f"倒数第二个台站: {stations[-2]}")

# 3. 列表切片
print("\n=== 列表切片 ===")
print(f"前三个台站: {stations[:3]}")
print(f"第2到第4个台站: {stations[1:4]}")
print(f"从第三个台站开始: {stations[2:]}")

# 4. 修改列表
print("\n=== 修改列表 ===")
print(f"原始台站列表: {stations}")
stations[1] = 'Nanjing'  # 修改第二个元素
print(f"修改后台站列表: {stations}")

# 5. 列表长度
print(f"\n台站数量: {len(stations)}")
print(f"震级数据数量: {len(magnitudes)}")

# 6. 列表常用方法
print("\n=== 列表常用方法 ===")
# 添加元素
stations.append('Xian')
print(f"添加西安后: {stations}")

# 在指定位置插入元素
stations.insert(2, 'Hangzhou')
print(f"在索引2插入杭州后: {stations}")

# 删除元素
removed_station = stations.pop()
print(f"删除最后一个台站 {removed_station} 后: {stations}")

# 删除指定元素
stations.remove('Nanjing')
print(f"删除南京后: {stations}")

# 排序
sorted_magnitudes = sorted(magnitudes)
print(f"原始震级: {magnitudes}")
print(f"排序后震级: {sorted_magnitudes}")

# 反转
magnitudes.reverse()
print(f"反转后震级: {magnitudes}")

# 7. 检查元素是否存在
print("\n=== 检查元素 ===")
print(f"北京是否在台站列表中: {'Beijing' in stations}")
print(f"上海是否在台站列表中: {'Shanghai' in stations}")

# 8. 列表与字符串转换
print("\n=== 列表与字符串转换 ===")
station_string = ', '.join(stations)
print(f"台站字符串: {station_string}")

new_stations = station_string.split(', ')
print(f"从字符串转换回列表: {new_stations}")