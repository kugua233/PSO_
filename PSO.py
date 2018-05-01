# coding: utf-8
from Initialization import init_population
import numpy as np
import math
import random
import matplotlib.pyplot as plt
"""
:parameter setting
"""
pop_size = 100
max_gen = 100
dec_num = 2
obj_num = 1
dec_min_val = (-3, 4.1)
dec_max_val = (12.1, 5.8)
w = 0.4  # 自身权重因子
c1 = 2  # 学习因子
c2 = 2
pop_x = np.zeros((pop_size, dec_num))  # 所有粒子的位置
pop_v = np.zeros((pop_size, dec_num))  # 所有粒子的速度
p_best = np.zeros((pop_size, dec_num))  # 个体经历的最佳位置和全局最佳位置
g_best = np.zeros((1, dec_num))
popobj = []


def fitness(s):
    x1 = s[0]
    x2 = s[1]
    y = 21.5 + x1 * math.sin(4 * math.pi * x1) + x2 * math.sin(20 * math.pi * x2)
    return y


if __name__ == '__main__':
    init_population(pop_size, dec_num, dec_min_val, dec_max_val, pop_x, pop_v, p_best)
    temp = -1
    for i in range(pop_size):   # 更新全局最优
        fit = fitness(p_best[i])
        if fit > temp:
            g_best = p_best[i]
            temp = fit
    print(fitness(g_best))
    for i in range(max_gen):
        for j in range(pop_size):
            #   ----------------更新个体位置和速度-----------------
            pop_v[j] = w * pop_v[j] + c1 * random.uniform(0, 1) * (p_best[j] - pop_x[j]) + \
                        c2 * random.uniform(0, 1) * (g_best - pop_x[j])
            pop_x[j] = pop_x[j] + pop_v[j]
            for k in range(dec_num):    # 越界保护
                if pop_x[j][k] < dec_min_val[k]:
                    pop_x[j][k] = dec_min_val[k]
                if pop_x[j][k] > dec_max_val[k]:
                    pop_x[j][k] = dec_max_val[k]
            #   -----------------更新p_best和g_best-----------------
            if fitness(pop_x[j]) > fitness(p_best[j]):
                p_best[j] = pop_x[j]
            if fitness(pop_x[j]) > fitness(g_best):
                g_best = pop_x[j]
        popobj.append(fitness(g_best))
        print(fitness(g_best))

    # -------------------画图--------------------
    plt.figure(1)
    plt.title("Figure1")
    plt.xlabel("iterators", size=14)
    plt.ylabel("fitness", size=14)
    t = [t for t in range(0, 100)]
    plt.plot(t, popobj, color='b', linewidth=3)
    plt.show()




