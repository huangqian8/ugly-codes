"""
BMI（Body Mass Index） 身体质量指数
通过人体体重和身高两个数值获得相对客观的参数，并用这个参数所处范围衡量身体质量。
计算公式：体重指数BMI=体重/身高的平方（国际单位kg/㎡）
"""


def bmi(height, weight):
    return weight / (height * height)

height = float(input('请输入身高（单位：米）: '))
weight = int(input('请输入体重（单位：公斤）： '))
print()
bmi = bmi(height, weight)
print('*******************************')
print('体重指数BMI为%.2f' % bmi)
if bmi < 18.5:
    print('体型偏瘦，请增加营养')
elif bmi >= 18.5 and bmi < 23.9:
    print('体型正常，请继续保持')
elif bmi >= 24 and bmi < 26.9:
    print('体型偏胖，请注意饮食')
elif bmi >= 27 and bmi < 29.9:
    print('体型肥胖，请加强锻炼')
else:
    print('体型重度肥胖，请及时就医')
print('*******************************')
