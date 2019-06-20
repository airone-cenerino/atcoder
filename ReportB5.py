import random
import math
import matplotlib.pyplot as plt


def divideTen(num):
    return num / 10


def divideSampleNum(num):
    return num / sampleNum * 10


average = 0
variance = [1, 5, 10]
sampleNum = 1000000

xAxis = list(
    map(divideTen, list(range(-100 + average * 10, 100 + average * 10))))


for j in range(3):
    li = list()
    for i in range(sampleNum):
        x = random.random()
        y = random.random()
        li.append(math.sqrt(variance[j] * -2 * math.log(x))
                  * math.cos(2 * math.pi * y) + average)

    yAxis = list()
    for i in range(len(xAxis)-1):
        yAxis.append(sum(x >= xAxis[i] and x < xAxis[i+1] for x in li))
    yAxis.append(sum(x >= xAxis[len(xAxis)-1] and x < 2 *
                     xAxis[len(xAxis) - 1] - xAxis[len(xAxis) - 2] for x in li))

    yAxis = list(map(divideSampleNum, yAxis))
    plt.plot(xAxis, yAxis)

plt.show()
