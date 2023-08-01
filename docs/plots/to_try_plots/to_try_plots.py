#python program to create visualisations for blog post 'Endeavour' of the to_try.html file.


import numpy as np
import matplotlib.pyplot as plt
from scipy import linspace
from scipy import pi,sqrt,exp
from scipy.special import erf

from pylab import plot,show
#import brainplotlib

def pdf(x):
    return 1/np.lib.scimath.sqrt(2*pi) * np.exp(-x**2/2)

def cdf(x):
    return (1+erf(x/np.lib.scimath.sqrt(2))) / 2

def skew(x, e=0,w=1,a=0):
    t=(x-e) / w
    return 2 / w * pdf(t) * cdf(a*t)


#create N = 100 equally spaced points between -5 and 5
N = 1000
x = np.linspace(0, 100, N)


e = 30.0 #location
w = 30.0 #scale
a = 0

p = skew(x, e, w, a)

plot(x, p)


#plt.plot(x, data)\
plt.ylim([0, 1.2*np.max(p)])
plt.ylabel('Intensity')
plt.xlim([np.min(x), np.max(x)])
plt.xlabel('Time')
plt.xticks([])
plt.yticks([])
#plt.savefig('plots/to_try_plots/intensity-time.jpg')
plt.show()


