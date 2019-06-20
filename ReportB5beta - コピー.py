import random
import math
import matplotlib.pyplot as plt
import numpy as np


def divideSampleNum(num):
    return num / sampleNum


average = 0
variance = [1, 5, 10]

sampleNum = 1000000

xAxis = list(map(divideSampleNum, list(range(sampleNum))))

x = np.random.normal(50, 10, 100000)
plt.hist(x, bins=200)
plt.show()
