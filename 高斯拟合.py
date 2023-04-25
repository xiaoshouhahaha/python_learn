import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def gaussian(x, amplitude, mean, stddev):
    return amplitude * np.exp(-((x - mean) / stddev) ** 2)


# 从文件中读取数据到x和y数组中
x = np.loadtxt('归一化焦点值.txt')
y = np.loadtxt('归一化清晰度.txt')

# 进行高斯曲线拟合
popt, pcov = curve_fit(gaussian, x, y, p0=[np.max(y), np.argmax(y), 1])

# 输出拟合曲线的最值和最值位置以及其他参数
print("最大值：", popt[0])
print("最大值位置：", popt[1])
print("标准差：", popt[2])

# 绘制原始数据和拟合曲线
plt.scatter(x, y, label='data')
plt.plot(x, gaussian(x, *popt), label='fit', color='r')

# 标注出拟合曲线的最大值位置
plt.annotate(f"max={popt[0]:.2f}", xy=(popt[1], popt[0]), xytext=(
    popt[1], popt[0]+1), ha='center', fontsize=10, arrowprops=dict(facecolor='black', shrink=0.05))

plt.legend()
plt.show()
