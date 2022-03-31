"""
    Use NFGS to solve optimization problem
        In this part, you can see two def: bfgs_newton and dfp_newton.
    Before you run the code, you need to know which function and how
    many unknowns paras you need to solve, then prepare the initial 
    values(x)、Primitive Function(f) and Jocobian Matrix(jacobian).
    And you can see an example in the last section.
"""

import numpy as np
from sympy import symbols


def bfgs_newton(f, x, n, iters):
    """
    BFGS method
        :param f: the Primitive Function needed to solve
        :param x: the Initial values(n dims)
        :param n: the Number of unknowns
        :param iters: Maximum number of Iterations
        :return: x value
    """
    # 步长。设为1才能收敛，小于1不能收敛
    learning_rate = 1
    # 初始化B正定矩阵
    B = np.eye(n)
    x_len = x.shape[0]
    # 一阶导g的第二范式的最小值（阈值）
    epsilon = 1e-5
    for i in range(1, iters):
        g = jacobian(f, x)
        if np.linalg.norm(g) < epsilon:
            break
        p = np.linalg.solve(B, g)
        # 更新x值
        x_new = x - p*learning_rate
        print("第" + str(i) + "次迭代后的结果为:", x_new)
        g_new = jacobian(f, x_new)
        y = g_new - g
        k = x_new - x
        y_t = y.reshape([x_len, 1])
        Bk = np.dot(B, k)
        k_t_B = np.dot(k, B)
        kBk = np.dot(np.dot(k, B), k)
        # 更新B正定矩阵。完全按照公式来计算
        B = B + y_t*y/np.dot(y, k) - Bk.reshape([x_len, 1]) * k_t_B / kBk
        x = x_new
    return x


def dfp_newton(f, x, n, iters):
    """
    DFP method
        :param f: the Primitive Function needed to solve
        :param x: the Initial values(n dims)
        :param n: the Number of unknowns
        :param iters: Maximum number of Iterations
        :return: x value
    """
    # 步长
    learning_rate = 1
    # 初始化B正定矩阵
    G = np.eye(n)
    x_len = x.shape[0]
    # 一阶导g的第二范式的最小值（阈值）
    epsilon = 1e-5
    for i in range(1, iters):
        g = jacobian(f, x)
        if np.linalg.norm(g) < epsilon:
            break
        p = np.dot(G, g)
        # 更新x值
        x_new = x - p * learning_rate
        print("第" + str(i) + "次迭代后的结果为:", x_new)
        g_new = jacobian(f, x_new)
        y = g_new - g
        k = x_new - x
        Gy = np.dot(G, y)
        y_t_G = np.dot(y, G)
        yGy = np.dot(np.dot(y, G), y)
        # 更新G正定矩阵
        G = G + k.reshape([x_len, 1]) * k / np.dot(k, y) - Gy.reshape([x_len, 1]) * y_t_G / yGy
        x = x_new
    return x


if __name__ == "__main__":
    ## 
    def jacobian(f, x):
        """
        Define A jocobian matrix
            Calculate the First Order Derivative of the Primitive Function
        :param f: the Primitive Function needed to solve
        :param x: Input values when Iterating
        :return: the vector of gradient
        """
        dfdx1 = 2*(x[0]-10)
        dfdx2 = 4*(x[1]-12)
        dfdx3 = 8*(x[2]-8)
        gradient = np.array([dfdx1, dfdx2, dfdx3], dtype=float)
        return gradient

    # First, define the elements of a three-dimensional vector
    x1 = symbols("x1")
    x2 = symbols("x2")
    x3 = symbols("x3")
    x = np.array([1, 1, 1], dtype=float)
    f = (x1-10)**2+2*(x2-12)**2+4*(x3-8)**2

    print(bfgs_newton(f, x, 3, 2000))
    print(dfp_newton(f, x, 3, 1000))
