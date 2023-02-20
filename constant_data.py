import json
from datetime import datetime, timedelta

# 设定起始日期和结束日期
start_date = datetime(2017, 1, 1)
end_date = datetime(2022, 12, 31)

# 定义每天的碳排放量
daily_emissions = 100

# 生成日期和对应的碳排放量，并添加到一个列表中
data = []
current_date = start_date
while current_date <= end_date:
    data.append({
        "date": current_date.strftime("%Y-%m-%d"),
        "value": daily_emissions
    })
    current_date += timedelta(days=1)

# 将列表中的数据存储为JSON格式的文件
with open("constant_trend.json", "w") as f:
    json.dump(data, f)
