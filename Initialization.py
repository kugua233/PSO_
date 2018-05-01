import random

def init_population(pop_size, dec_num, dec_min_val, dec_max_val, pop_x, pop_v, p_best):
    for i in range(pop_size):
        for j in range(dec_num):
            pop_x[i][j] = random.uniform(dec_min_val[j], dec_max_val[j])
            pop_v[i][j] = random.uniform(0, 1)
        p_best[i] = pop_x[i]  # p_best存储个体的历史最优
