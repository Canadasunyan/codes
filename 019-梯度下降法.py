import numpy as np

# 生成数据模型
# 1. y(t) = 0.4 * y(t-3) + 0.7 * y(t-2) + 1.3 * y(t-1) + epsilon, length = 10
# 2. y(t) = 0.4 * y(t-3) + 0.4 * y(t-2) + 0.3 * y(t-1) + epsilon, length = 120
def generate_y(array_length):
    x = [0.1, 0.1, 0.1]
    for i in range(array_length):
        m = x[-1] * 1.3 + x[-2] * 0.7 + x[-3] * 0.4 + epsilon
        x.append(m)
    print(x)
    return np.array(x)

# 计算residual
def computeResidual(alpha, beta, x, y):
    '''
    alpha: List(float)
    beta: List(float)
    x: np.array(float), shape = (2, 12)
    y: np.array(float), shape = (1, 15)
    '''
    func = lambda a, b: a * b
    diff_ls = np.zeros(len(x[0]))
    residual = 0
    for index in range(3, len(y)):
        diff = y[index] - sum(list(map(func, alpha, y[index-3:index]))) - beta[0] * x[0][index - 3] - beta[1] * x[1][index - 3]
        diff_ls[index - 3] = diff
        residual += diff * diff
    # residual_ls[0] = (y3 - a0y0 - a1y1 - a2y2 - b0x[0][3] - b1x[1][3])^2
    return diff_ls, residual / len(x[0])


def computeGradient(alpha, beta, x, y, lam=0.1):
    grad_alpha = np.array([0., 0., 0.])
    grad_beta = np.array([0., 0.])
    length = len(x[0])
    diff_ls, residual = computeResidual(alpha, beta, x, y)
    # for index in range(len(y)-3):
        grad_alpha = np.array()
        # for i in range(len(grad_alpha)):
            # 计alpha1和alpha2梯度
            d = 2 * y[index + i] * diff_ls[index]
            grad_alpha[i] -= d / length + lam * [1, -1][d < 0] / length
        # for j in range(len(x)):
            # 计算beta1和beta2梯度
            d = 2 * x[0][index] * diff_ls[index]
            grad_beta[j] -= d / length + lam * [1, -1][d < 0] / length
        # assign
    return grad_alpha, grad_beta

def GradientDescent(alpha, beta, grad_alpha, grad_beta, learning_rate=0.0001):
    alpha -= learning_rate * grad_alpha
    beta -= learning_rate * grad_beta
    print('grad_a:', grad_alpha, 'grad_b:', grad_beta)
    print('alpha:', alpha, 'beta:', beta)
    return alpha, beta


if __name__ == "__main__":
    array_length = 10
    x = 10 * np.random.rand(2, array_length)
    y = generate_y(array_length)
    learning_rate = 0.001
    alpha = np.array([0., 0., 0.])
    beta = np.array([0., 0.])
    epsilon = 0.00001
    improvement = computeResidual(alpha, beta, x, y)[1]
    previous_residual = 10000
    i = 0
    while improvement > epsilon or improvement < -epsilon:
        diff_ls, residual = computeResidual(alpha, beta, x, y)
        print('Residual=', residual)
        improvement = previous_residual - residual
        print('Improvement=', improvement)
        grad_alpha, grad_beta = computeGradient(alpha, beta, x, y)
        print('Epoch ', i)
        i += 1
        alpha, beta = GradientDescent(alpha, beta, grad_alpha, grad_beta, learning_rate)
        previous_residual = residual

Lasso


