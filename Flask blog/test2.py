#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from random import choice
import matplotlib
# matplotlib.rcParams['font.sans-serif'] = ['SemiHei'] #指定默认字体
# matplotlib.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题

# eqs = ['World','Python',"Mxl"]
#边框边界
# for i in range(24):
#     index = np.random.randint(0,len(eqs))
#     eq = eqs[index]
#     size = np.random.uniform(2,16)
#     x,y = np.random.uniform(0,1,2)
#     alpha = np.random.uniform(0.25,0.75)
#     plt.text(x, y, eq, ha='center', va='center', color=choice(["#11557c","#0A5CD6","#FEFFFF","#020034"]), alpha=alpha,
#              transform=plt.gca().transAxes, fontsize=size, clip_on=True)
plt.axes([0, 0, 1, 1])
for i in range(100):
    ab_range_low = 0.0
    ab_range_high = 30.0
    a = np.random.uniform(ab_range_low,ab_range_high)
    b = np.random.uniform(ab_range_low,ab_range_high)

    pi_range_low = 1
    pi_range_high = 10
    pi_x = choice([-np.pi/choice(range(pi_range_low,pi_range_high)), np.pi/choice(range(pi_range_low,pi_range_high))])
    pi_y = choice([np.pi/choice(range(pi_range_low,pi_range_high)), -np.pi/choice(range(pi_range_low,pi_range_high))])
    X = np.linspace(pi_x, pi_y, 256)
    x,y = choice([a*np.cos(X), -a*np.cos(X)]), choice([b*np.sin(X), -b*np.sin(X)])
    # x,y = a*np.cos(X), choice([b*np.sin(X), -b*np.sin(X)])
    # x,y = choice([a*np.cos(X), -a*np.cos(X)]), b*np.sin(X)
    alpha = np.random.uniform(0.15,0.75)
    linewidth = np.random.uniform(2.0,40.0)
    plt.plot(X, x, alpha=alpha, linestyle='-', linewidth=linewidth, color=choice(["#11557c", "#0A5CD6", "#FEFFFF", "#020034"]))
    # plt.plot(X, y, alpha=alpha, linestyle='-', linewidth=linewidth, color=choice(["#11557c", "#0A5CD6", "#FEFFFF", "#020034"]))
    # plt.plot(x, y, alpha=alpha, linestyle='-', linewidth=linewidth, color=choice(["#11557c", "#0A5CD6", "#FEFFFF", "#020034", "#FFA500", "#98FB98", "#00FFFF"]))


plt.xticks(), plt.yticks()
plt.savefig('num.png', dpi=256)
plt.show()