import json

# 默认的服务器硬件配置列表
server_configurations = {
    'A': 10,
    'B': 8,
    'C': 6,
    'D': 4,
    'E': 2
}

# 默认的能源类型列表
energy_types = {
    'Coal': 10,
    'Natural gas': 8,
    'Hydro': 6,
    'Wind': 4,
    'Solar': 2
}

# 读取JSON文件中的数据
with open('carbon_data.json', 'r') as f:
    carbon_data = json.load(f)

# 获取最后一天的碳排放数据
last_day_data = carbon_data[-1]

# 判断是否需要改进
if last_day_data['value'] > 100:
    # 碳排放量过大，需要改进
    print("建议：")
    # 优先使用能清洁的能源
    for energy_type, value in energy_types.items():
        if value < last_day_data['energy_type_value']:
            print(f"使用更清洁的能源：{energy_type}")
            break
    # 增加服务器使用率
    if last_day_data['server_usage'] < 100:
        print(f"增加服务器使用率：{last_day_data['server_usage'] + 10}%")
    # 减少服务器工作时间/每天（百分比）
    if last_day_data['server_work_time'] > 10:
        print(f"减少服务器工作时间/每天（百分比）：{last_day_data['server_work_time'] - 10}%")
    # 更换能耗能少的服务器硬件配置
    for server_configuration, value in server_configurations.items():
        if value < last_day_data['server_configuration_value']:
            print(f"更换能耗能少的服务器硬件配置：{server_configuration}")
            break
else:
    # 碳排放量很少，不需要改进
    print("无需改进。")
