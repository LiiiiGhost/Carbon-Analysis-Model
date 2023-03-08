import json

# 设置初始值和变化率
start_value = 100
increase_rate = 0.1

# 生成2017年到2022年每天的数据
data = []
for year in range(2020, 2023):
    for month in range(1, 13):
        # 处理不同月份的天数
        if month in [1, 3, 5, 7, 8, 10, 12]:
            days = 31
        elif month == 2:
            # 处理闰年的情况
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                days = 29
            else:
                days = 28
        else:
            days = 30
        for day in range(1, days+1):
            # 每天的数值为上一天的数值加上变化率
            start_value += increase_rate
            data.append({
                "date": f"{year}-{month:02d}-{day:02d}",
                "value": round(start_value, 2)
            })

# 将数据存储到json文件中
with open("increasing_data.json", "w") as f:
    json.dump(data, f)
