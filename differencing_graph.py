import json
import pandas as pd
import matplotlib.pyplot as plt

# 从 JSON 文件中读取数据
with open('carbon_emissions.json', 'r') as f:
    data = json.load(f)

# 转换为 Pandas DataFrame
df = pd.DataFrame(data)

# 将 date 列转换为 datetime 类型
df['date'] = pd.to_datetime(df['date'])

# 将 date 列设置为索引
df.set_index('date', inplace=True)

# 计算一阶差分和二阶差分
diff1 = df.diff()
diff2 = diff1.diff()

# 绘制原始数据、一阶差分、二阶差分的图形
fig, axs = plt.subplots(3, 1, figsize=(10, 10))
axs[0].plot(df.index, df['value'])
axs[0].set_title('Original Data')
axs[0].set_ylabel('CO2 Emissions')

axs[1].plot(diff1.index, diff1['value'])
axs[1].set_title('First Difference')
axs[1].set_ylabel('CO2 Emissions Change')

axs[2].plot(diff2.index, diff2['value'])
axs[2].set_title('Second Difference')
axs[2].set_ylabel('CO2 Emissions Change Rate')

plt.tight_layout()
plt.show()
