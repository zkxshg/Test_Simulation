#导入需要使用的工具包：numpy、sklearn、pandas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''
#使用pandas将数据作为矩阵读入
#x_matrix = np.loadtxt(open("x_demo.csv","rb"),delimiter=",",skiprows=1)

#确定均值
average = 50
#开始生产正态分布的随机数
#确定均值
mu = 50
#确定标准差
sigma = 15
#开始生成随机数
s = np.random.normal(mu, sigma, 10000)
#将均值调整为average
result = []
sumr = 2*average
for n in s:
    if n>=0 and n<=100:
        n1 = int(n)
        n2 = sumr - n1
        result.append(n1)
        result.append(n2)

# 对X进行重排序，如果X为多维数组，只沿第一条轴洗牌，输出为None。
np.random.shuffle(result)
#将预测结果输出到pre.txt中
np.savetxt("pre.csv", result, delimiter=",", fmt="%d")
'''
#读入外部成绩，并计算得到上锚点和下锚点
def get_realdata(chine,math,eng):
    total = chine + math + eng
    ysw = total
    p_95 = 450 * 0.95
    p_5 = 450 * 0.05
    ysw.sort()
    l = len(ysw)
    # print(ysw)
    i = 0
    j = 0
    for n in ysw:
        if n >= p_95:
            i += 1
        if n <= p_5:
            j += 1
    return i / l, j / l

def get_random(average,size,max):
    pass
#根据均值、考生数、满分和标准差生成仿真考生成绩
def get_sample(average, size,max,sigma):
    # 确定均值
    #average = 50
    # 开始生产正态分布的随机数
    # 确定均值
    mu = average
    print(max)
    # 确定标准差
    #sigma = 15
    # 开始生成随机数
    s = np.random.normal(mu, sigma, size)
    # 将均值调整为average
    result = []
    sumr = 2 * average
    for n in s:
        if n>= 0 and n<= max:
            if n<=sumr:
                if n>average:
                    n1 = int(n)
                    n2 = sumr - n1
                    result.append(n1)
                    result.append(n2)
                else:
                    n1 = int(n)
                    n2 = sumr - n1
                    result.append(n1)
                    if n2<=max:
                        result.append(n2)


            else:
                n1 = int(n)
                n2 = n3 = average - (n1 - average) / 2
                result.append(n1)
                result.append(n2)
                result.append(n3)


    #np.random.shuffle(result)
    # 将预测结果输出到pre.txt中
    return result


#以下是随机生成语数外/语数总分
resul = get_sample(150,10000,300,75)
resul.sort()
x_c = []
y_c = []
for i in range(0,300):
    j = 0
    for n in resul:
        if n==i:
            j+=1
    x_c.append(i)
    y_c.append(j)

plt.plot(x_c, y_c)
plt.show()

p_95 = 300 * 0.95
p_5 = 300 * 0.05
l = len(resul)
# print(ysw)
i = 0
j = 0
for n in resul:
    if n >= p_95:
        i += 1
    if n <= p_5:
        j += 1
print (l,i / l, j / l)
np.savetxt("pre.csv", resul, delimiter=",", fmt="%d")

