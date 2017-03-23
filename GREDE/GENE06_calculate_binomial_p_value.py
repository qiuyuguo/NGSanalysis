import numpy as np

n=468900
p=0.00018
k=244
combination_num = range(k+1, n+1)
combination_den = range(1, n-k+1)
combination_log = np.log10(combination_num).sum() - np.log10(combination_den).sum()
p_k_log = k * np.log10(p)
neg_p_K_log = (n - k) * np.log10(1 - p)
p_log = combination_log + p_k_log + neg_p_K_log
print(-p_log)
#probability = np.exp(p_log)
