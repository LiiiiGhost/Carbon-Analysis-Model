import json
import datetime

# 读取 JSON 文件
with open("UKI_DAI_DataEngineering_Discovery.json", "r") as f:
    data = json.load(f)

# 计算开始日期
start_date = datetime.datetime(2020, 1, 1, 0, 0, 0)

# 遍历字典列表
for i, d in enumerate(data):
    # 计算当前日期
    current_date = start_date + datetime.timedelta(days=i)

    # 将当前日期格式化为字符串
    current_date_str = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # 更新字典的日期
    d["date"] = current_date_str

# 将修改后的字典列表写入 JSON 文件
with open("new_UKI_DAI_DataEngineering_Discovery.json", "w") as f:
    json.dump(data, f)
