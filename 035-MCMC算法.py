# MCMC算法模拟Beta分布
import numpy as np
import scipy.special as ss
import matplotlib.pyplot as plt

def beta_raw(x, a, b):
    # 未归一化之前的概率密度函数
    return x**(a-1) * (1-x)**(b-1)
def beta(x, a, b):
    # 归一化, Beta(a, b)为常数
    return beta_raw(x, a, b) / ss.beta(a, b)

def plot_mcmc(a, b):
    # 初始化x0
    cur = np.random.rand()
    states = [cur]
    for i in range(10**5):
        next, u = np.random.rand(), np.random.rand()
        if u < np.min((beta_raw(next, a, b) / beta_raw(cur, a, b), 1)):
            states.append(next)
            cur = next
        else:
            states.append(cur)
    x = np.arange(0.001, 1, .001)
    plt.figure(figsize=(10, 5))
    # 真正的Beta分布
    plt.plot(x, beta(x, a, b), lw=2, label='real dist: a={}, b={}'.format(a, b))
    # 模拟结果
    plt.hist(states[-5000:], 25, density=True, label='simu mcmc: a={}, b={}'.format(a, b))
    plt.show()

if __name__ == '__main__':
    plot_mcmc(0.1, 0.1)
    plot_mcmc(1, 1)
    plot_mcmc(2, 3)