# 地震数据处理实际应用示例
# 结合列表和循环处理真实地震数据

# 1. 地震事件数据结构
print("=== 地震事件数据结构 ===")
earthquake_events = [
    {'date': '2023-12-20', 'location': 'Beijing', 'magnitude': 3.2, 'depth': 10.5, 'stations': ['BJI', 'BJT', 'SNY']},
    {'date': '2023-12-21', 'location': 'Shanghai', 'magnitude': 4.5, 'depth': 15.2, 'stations': ['SSE', 'NJ2', 'HZH']},
    {'date': '2023-12-22', 'location': 'Guangzhou', 'magnitude': 6.1, 'depth': 8.7, 'stations': ['GZH', 'QZH', 'SZX']},
    {'date': '2023-12-23', 'location': 'Shenzhen', 'magnitude': 2.8, 'depth': 12.3, 'stations': ['SZX', 'GZH', 'ZUH']},
    {'date': '2023-12-24', 'location': 'Chengdu', 'magnitude': 5.3, 'depth': 18.9, 'stations': ['CD2', 'GYA', 'XAN']}
]

# 2. 遍历地震事件列表
print("\n=== 地震事件报告 ===")
for event in earthquake_events:
    print(f"日期: {event['date']}")
    print(f"地点: {event['location']}")
    print(f"震级: {event['magnitude']}")
    print(f"深度: {event['depth']} km")
    print(f"记录台站: {', '.join(event['stations'])}")
    print("-" * 40)

# 3. 筛选强震事件
print("\n=== 强震事件筛选 (震级 >= 5.0) ===")
strong_earthquakes = []
for event in earthquake_events:
    if event['magnitude'] >= 5.0:
        strong_earthquakes.append(event)
        print(f"强震警告: {event['date']} {event['location']} M{event['magnitude']}")

print(f"\n共发现 {len(strong_earthquakes)} 次强震事件")

# 4. 统计分析
print("\n=== 地震数据统计分析 ===")
total_magnitude = 0
shallow_earthquakes = []  # 浅源地震 (深度 < 15km)
deep_earthquakes = []     # 深源地震 (深度 >= 15km)

for event in earthquake_events:
    total_magnitude += event['magnitude']
    
    if event['depth'] < 15:
        shallow_earthquakes.append(event)
    else:
        deep_earthquakes.append(event)

average_magnitude = total_magnitude / len(earthquake_events)
print(f"平均震级: {average_magnitude:.2f}")
print(f"浅源地震次数: {len(shallow_earthquakes)}")
print(f"深源地震次数: {len(deep_earthquakes)}")

# 5. 台站数据处理
print("\n=== 台站数据处理 ===")
# 收集所有记录到的台站
all_stations = []
for event in earthquake_events:
    for station in event['stations']:
        if station not in all_stations:  # 避免重复
            all_stations.append(station)

print(f"所有参与记录的台站: {', '.join(all_stations)}")
print(f"总台站数: {len(all_stations)}")

# 统计每个台站记录到的地震次数
station_counts = {}
for event in earthquake_events:
    for station in event['stations']:
        if station in station_counts:
            station_counts[station] += 1
        else:
            station_counts[station] = 1

print("\n各台站记录次数:")
for station, count in station_counts.items():
    print(f"{station}: {count} 次")

# 6. 地震波形数据处理
print("\n=== 地震波形数据处理 ===")
# 模拟一个地震事件的波形数据
sampling_rate = 100  # 采样率 (Hz)
duration = 30        # 持续时间 (秒)
num_samples = sampling_rate * duration

# 生成模拟波形数据 (这里用简单的正弦波模拟)
import math
waveform = []
time_points = []

for i in range(num_samples):
    time = i / sampling_rate
    time_points.append(time)
    
    # 模拟P波和S波到达
    p_wave_time = 5.0   # P波到达时间
    s_wave_time = 8.0   # S波到达时间
    
    amplitude = 0.1  # 背景噪声
    
    if time > p_wave_time:
        # P波信号
        amplitude += 0.5 * math.sin(2 * math.pi * 10 * (time - p_wave_time)) * math.exp(-0.5 * (time - p_wave_time))
    
    if time > s_wave_time:
        # S波信号 (振幅更大)
        amplitude += 1.0 * math.sin(2 * math.pi * 5 * (time - s_wave_time)) * math.exp(-0.3 * (time - s_wave_time))
    
    waveform.append(amplitude)

# 检测地震信号
threshold = 0.3  # 检测阈值
signal_detected = False
detection_times = []

for i, amplitude in enumerate(waveform):
    if amplitude > threshold and not signal_detected:
        # 检测到信号开始
        signal_detected = True
        detection_time = time_points[i]
        detection_times.append(detection_time)
        print(f"检测到信号开始于 {detection_time:.2f} 秒")
    elif amplitude <= threshold and signal_detected:
        # 信号结束
        signal_detected = False

# 7. 批量处理多个台站数据
print("\n=== 批量处理多个台站数据 ===")
station_data = {
    'BJI': {'max_amplitude': 1.2, 'p_arrival': 5.1, 's_arrival': 8.2},
    'BJT': {'max_amplitude': 0.8, 'p_arrival': 5.3, 's_arrival': 8.5},
    'SNY': {'max_amplitude': 0.6, 'p_arrival': 5.5, 's_arrival': 8.8},
    'SSE': {'max_amplitude': 2.1, 'p_arrival': 4.8, 's_arrival': 7.9},
    'NJ2': {'max_amplitude': 1.5, 'p_arrival': 5.0, 's_arrival': 8.1}
}

print("台站数据处理结果:")
for station_code, data in station_data.items():
    # 计算S-P时间差 (用于定位)
    sp_diff = data['s_arrival'] - data['p_arrival']
    
    # 评估信号质量
    if data['max_amplitude'] > 1.5:
        quality = "优秀"
    elif data['max_amplitude'] > 1.0:
        quality = "良好"
    else:
        quality = "一般"
    
    print(f"{station_code}: 最大振幅={data['max_amplitude']:.1f}, S-P时间差={sp_diff:.1f}s, 信号质量={quality}")

# 8. 数据导出格式化
print("\n=== 数据导出格式化 ===")
# 将地震事件数据导出为CSV格式
csv_lines = ["日期,地点,震级,深度,台站数量"]
for event in earthquake_events:
    line = f"{event['date']},{event['location']},{event['magnitude']},{event['depth']},{len(event['stations'])}"
    csv_lines.append(line)

print("CSV格式数据:")
for line in csv_lines:
    print(line)

# 保存到文件
with open('earthquake_data.csv', 'w', encoding='utf-8') as f:
    for line in csv_lines:
        f.write(line + '\n')

print("\n数据已保存到 earthquake_data.csv 文件")