# Python列表和循环练习题
# 地震数据处理应用

# 练习1: 基本列表操作
print("=== 练习1: 基本列表操作 ===")
# 已知地震震级列表
magnitudes = [3.2, 4.5, 6.1, 2.8, 5.3, 4.0, 3.7, 5.8]

# 1.1 计算并打印震级列表的长度
print(f"震级数据数量: {len(magnitudes)}")

# 1.2 找出并打印最大震级和最小震级
max_magnitude = max(magnitudes)
min_magnitude = min(magnitudes)
print(f"最大震级: {max_magnitude}")
print(f"最小震级: {min_magnitude}")

# 1.3 计算并打印平均震级
average_magnitude = sum(magnitudes) / len(magnitudes)
print(f"平均震级: {average_magnitude:.2f}")

# 1.4 找出所有震级大于4.0的地震
strong_earthquakes = []
for magnitude in magnitudes:
    if magnitude > 4.0:
        strong_earthquakes.append(magnitude)
print(f"震级大于4.0的地震: {strong_earthquakes}")

# 使用列表推导式重写1.4
strong_earthquakes_comp = [magnitude for magnitude in magnitudes if magnitude > 4.0]
print(f"使用列表推导式: {strong_earthquakes_comp}")

# 练习2: 列表和循环结合
print("\n=== 练习2: 列表和循环结合 ===")
# 已知地震事件数据
earthquake_events = [
    {'date': '2023-12-20', 'location': 'Beijing', 'magnitude': 3.2, 'depth': 10.5},
    {'date': '2023-12-21', 'location': 'Shanghai', 'magnitude': 4.5, 'depth': 15.2},
    {'date': '2023-12-22', 'location': 'Guangzhou', 'magnitude': 6.1, 'depth': 8.7},
    {'date': '2023-12-23', 'location': 'Shenzhen', 'magnitude': 2.8, 'depth': 12.3},
    {'date': '2023-12-24', 'location': 'Chengdu', 'magnitude': 5.3, 'depth': 18.9}
]

# 2.1 打印所有地震事件的基本信息
print("地震事件列表:")
for event in earthquake_events:
    print(f"日期: {event['date']}, 地点: {event['location']}, 震级: {event['magnitude']}, 深度: {event['depth']}km")

# 2.2 筛选出所有浅源地震(深度<15km)
shallow_earthquakes = []
for event in earthquake_events:
    if event['depth'] < 15:
        shallow_earthquakes.append(event)
print(f"\n浅源地震(深度<15km):")
for event in shallow_earthquakes:
    print(f"{event['date']} {event['location']} M{event['magnitude']} 深度{event['depth']}km")

# 2.3 按震级从大到小排序
sorted_events = sorted(earthquake_events, key=lambda x: x['magnitude'], reverse=True)
print("\n按震级排序的地震事件:")
for event in sorted_events:
    print(f"{event['location']}: M{event['magnitude']}")

# 练习3: 嵌套列表处理
print("\n=== 练习3: 嵌套列表处理 ===")
# 地震台站网络数据
seismic_networks = [
    {'name': '华北网络', 'stations': ['BJI', 'BJT', 'SNY', 'TAY', 'ZHH']},
    {'name': '华东网络', 'stations': ['SSE', 'NJ2', 'HZH', 'FZ1', 'QZH']},
    {'name': '华南网络', 'stations': ['GZH', 'SZX', 'QZH', 'ZUH', 'HUY']},
    {'name': '西南网络', 'stations': ['CD2', 'GYA', 'XAN', 'LZH', 'KMI']}
]

# 3.1 计算每个网络的台站数量
for network in seismic_networks:
    print(f"{network['name']}: {len(network['stations'])} 个台站")

# 3.2 收集所有不重复的台站代码
all_stations = []
for network in seismic_networks:
    for station in network['stations']:
        if station not in all_stations:
            all_stations.append(station)
print(f"\n所有台站代码: {', '.join(all_stations)}")
print(f"总台站数: {len(all_stations)}")

# 3.3 统计每个台站代码出现的次数
station_counts = {}
for network in seismic_networks:
    for station in network['stations']:
        if station in station_counts:
            station_counts[station] += 1
        else:
            station_counts[station] = 1

print("\n台站代码出现次数:")
for station, count in station_counts.items():
    print(f"{station}: {count} 次")

# 练习4: 实际应用场景
print("\n=== 练习4: 实际应用场景 ===")
# 模拟24小时地震监测数据
hourly_counts = [0, 0, 1, 0, 2, 1, 3, 2, 4, 3, 2, 1, 1, 0, 2, 1, 1, 0, 1, 2, 1, 0, 0, 1]

# 4.1 计算总地震次数
total_earthquakes = sum(hourly_counts)
print(f"24小时内总地震次数: {total_earthquakes}")

# 4.2 找出地震最活跃的小时
max_count = max(hourly_counts)
max_hour = hourly_counts.index(max_count)
print(f"地震最活跃的小时: {max_hour}:00 (共{max_count}次)")

# 4.3 计算平均每小时地震次数
average_per_hour = total_earthquakes / len(hourly_counts)
print(f"平均每小时地震次数: {average_per_hour:.2f}")

# 4.4 找出所有没有地震的小时
quiet_hours = []
for hour, count in enumerate(hourly_counts):
    if count == 0:
        quiet_hours.append(hour)
print(f"没有地震的小时: {quiet_hours}")

# 4.5 创建地震活跃度报告
print("\n地震活跃度报告:")
for hour, count in enumerate(hourly_counts):
    if count == 0:
        status = "安静"
    elif count <= 2:
        status = "正常"
    else:
        status = "活跃"
    print(f"{hour:02d}:00 - {count}次地震 ({status})")

# 练习5: 挑战题
print("\n=== 练习5: 挑战题 ===")
# 地震波形数据处理
waveform_data = [0.1, 0.2, 0.15, 0.3, 0.8, 1.2, 1.5, 1.3, 0.9, 0.4, 0.2, 0.1, 
                0.15, 0.25, 0.35, 0.5, 0.7, 0.9, 1.1, 1.0, 0.8, 0.6, 0.4, 0.2]

# 5.1 找出波形中的最大振幅及其位置
max_amplitude = max(waveform_data)
max_index = waveform_data.index(max_amplitude)
print(f"最大振幅: {max_amplitude}, 出现在位置: {max_index}")

# 5.2 计算平均振幅
average_amplitude = sum(waveform_data) / len(waveform_data)
print(f"平均振幅: {average_amplitude:.3f}")

# 5.3 统计振幅超过阈值的数据点数量
threshold = 0.8
exceed_count = 0
exceed_indices = []
for i, amplitude in enumerate(waveform_data):
    if amplitude > threshold:
        exceed_count += 1
        exceed_indices.append(i)
print(f"振幅超过{threshold}的数据点: {exceed_count}个")
print(f"这些数据点的位置: {exceed_indices}")

# 5.4 计算信号的信噪比(SNR)
# 假设前5个点和后5个点是噪声，中间是信号
noise_segment = waveform_data[:5] + waveform_data[-5:]
signal_segment = waveform_data[5:-5]

noise_power = sum([x**2 for x in noise_segment]) / len(noise_segment)
signal_power = sum([x**2 for x in signal_segment]) / len(signal_segment)
snr = signal_power / noise_power if noise_power > 0 else float('inf')

print(f"信号功率: {signal_power:.4f}")
print(f"噪声功率: {noise_power:.4f}")
print(f"信噪比(SNR): {snr:.2f}")

print("\n=== 练习完成 ===")
print("恭喜您完成了所有练习！这些例子展示了列表和循环在地震数据处理中的实际应用。")