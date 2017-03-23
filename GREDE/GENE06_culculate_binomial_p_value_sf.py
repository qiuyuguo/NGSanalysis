n=468900
p=0.00018
x=244

from scipy.stats import norm
the_scale=sqrt(n*p*(1-p))
the_loc=n*p
# survival function = 1 - cdf
output=-norm.logsf(x, loc=the_loc, scale=the_scale)
norm.logcdf(x, loc=the_loc, scale=the_scale)
print(output)