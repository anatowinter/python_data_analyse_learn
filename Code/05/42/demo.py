import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
df1=pd.read_excel('data.xls')              #导入Excel文件
#绘制折线图
sns.lineplot(x="学号", y="语文",data=df1)
plt.show()# 显示
