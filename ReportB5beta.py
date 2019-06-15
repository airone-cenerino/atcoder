import random
import math
import matplotlib.pyplot as plt


def divideSampleNum(num):
    return num / sampleNum


average = 0
variance = [1, 5, 10]

sampleNum = 1000000

xAxis = list(map(divideSampleNum, list(range(sampleNum))))

for j in range(3):
    li = list()

    for i in range(sampleNum):
        x = random.random()
        y = random.random()
        li.append(math.sqrt(variance[j] * -2 * math.log(x))
                  * math.cos(2 * math.pi * y) + average)

    li.sort()
    plt.plot(li, xAxis)
plt.show()
