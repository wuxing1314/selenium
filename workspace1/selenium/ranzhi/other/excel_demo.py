'''
workbook 工作簿
wroksheet 工作表
cell    单元格
'''
import openpyxl

# 打开工作簿
workbook = openpyxl.load_workbook(r'selenium\ranzhi\data.xlsx')
# 获取指定的工作表
worksheet = workbook['login_success']

# [('admin','123456','admin'),('user1','123456','user1')]
# 遍历行
# 方法一
# data = []
# for row in worksheet:
#     # 遍历行中每一个单元格
#     r = []
#     for cell in row:
#         # 获取单元格中的数据
#         r.append(cell.value)
#     data.append(tuple(r))
# print(data)

# 方法二
data = [tuple(cell.value for cell in row) for row in worksheet]
print(data)