#Derived from https://datasciencechalktalk.com/2019/09/02/hypothesis-tests-with-python/

import numpy as np

# Create population with mean of 1.5
sample_mean, sample_sigma = 1.5, 2
sample = np.random.normal(sample_mean, sample_sigma, 200)



# Create data sample with a mean of 3
mu, sigma = 3, 2 
s = np.random.normal(mu, sigma, 10000)

# Set plot settings and queue plots for rendering
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 30, alpha=0.1, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')

sample_count, sample_bins, sample_ignored = plt.hist(sample, 30, alpha=0.1, color='r',density=True)
plt.plot(sample_bins,1/(sample_sigma * np.sqrt(2 * np.pi)) *np.exp( - (sample_bins - sample_mean)**2 / (2 * sample_sigma**2) ),linewidth=2, color='r')
plt.plot(bins,1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='b')

#Plot 95% confidence interval lines
import scipy
from scipy import stats, optimize, interpolate
ci = scipy.stats.norm.interval(0.95, loc=1.5, scale=2)
plt.axvline(ci[0],color='g')
plt.axvline(ci[1],color='g')

#Label possible outcomes of test
plt.fill_between(x=np.arange(-4,ci[0],0.01), 
                 y1= scipy.stats.norm.pdf(np.arange(-4,ci[0],0.01),loc=1.5,scale=2) ,
                 facecolor='red',
                 alpha=0.35)

plt.fill_between(x=np.arange(ci[1],7.5,0.01), 
                 y1= scipy.stats.norm.pdf(np.arange(ci[1],7.5,0.01),loc=1.5,scale=2) ,
                 facecolor='red',
                 alpha=0.5)

plt.fill_between(x=np.arange(ci[0],ci[1],0.01), 
                 y1= scipy.stats.norm.pdf(np.arange(ci[0],ci[1],0.01),loc=3, scale=2) ,
                 facecolor='blue',
                 alpha=0.5)

plt.text(x=0, y=0.18, s= "Null Hypothesis")
plt.text(x=6, y=0.05, s= "Alternative")
plt.text(x=-4, y=0.01, s= "Type 1 Error")
plt.text(x=6.2, y=0.01, s= "Type 1 Error")
plt.text(x=2, y=0.02, s= "Type 2 Error")

# Render all plots
plt.show()