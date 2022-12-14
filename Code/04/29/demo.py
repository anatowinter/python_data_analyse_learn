import pandas as pd
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df=pd.read_excel('grade.xls')      #导入Excel文件
df = df.set_index(['班级','序号']) #设置2级索引“班级”和“序号”
df = df.stack()
print(df)
