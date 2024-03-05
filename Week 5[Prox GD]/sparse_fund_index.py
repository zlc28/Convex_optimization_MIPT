import numpy as np

# number of stocks
n = 500
# number of factors (not described or needed in problem statement)
k = 20

# generate rbar, Sigma
# factor matrix, entries uniform on [-0.5,1]
F = 1.5 * np.random.rand(n, k) - 0.5
Sigma = 0.5 * F @ np.diag(np.random.rand(k)) @ F.T + np.diag(0.1 * np.random.rand(n))
# risk-free return (weekly, 5% annual)
mu_rf = 0.2
# Sharpe ratio
SR = 0.4
# expected return
rbar = mu_rf + SR * np.sqrt(np.diag(Sigma))
# market capitalization (index weights)
c = 5 + np.exp(2 * np.random.randn(n))
