import random
import math
import matplotlib.pyplot as plt


def divideTen(num):
    return num/10


print("Input average : ", end="")
average = int(input())
print("Input variance : ", end="")
variance = int(input())

# li = list()
# xAxis = list(range(-100 + average * 10, 100 + average * 10))
# xAxis = list(map(divideTen, xAxis))

# for i in range(10000):
#     x = random.random()
#     y = random.random()sampleNum = 10000
li = list()
xAxis = list(
    map(divideTen, list(range(-100 + average * 10, 100 + average * 10))))
sampleNum = 10000
li = list()
xAxis = list(
    map(divideTen, list(range(-100 + average * 10, 100 + average * 10))))
sampleNum = 10000
li = list()
xAxis = list(
    map(divideTen, list(range(-100 + average * 10, 100 + average * 10))))
sampleNum = 10000
li = list()
xAxis = list(
    map(divideTen, list(range(-100 + average * 10, 100 + average * 10))))
sampleNum = 10000
li = list()
xAxis = list(
    map(divideTen, list(range(-100 + average * 10, 100 + average * 10))))
sampleNum = 10000
li = list()
xAxis = list(
    map(divideTen, list(range(-100 + average * 10, 100 + average * 10))))
sampleNum = 10000
li = list()
xAxis = list(
    map(divideTen, list(range(-100 + average * 10, 100 + average * 10))))
sampleNum = 10000
li = list()
xAxis = list(
    map(divideTen, list(range(-100 + average * 10, 100 + average * 10))))

#     li.append(variance * math.sqrt(-2*math.log(x))
#               * math.cos(2*math.pi*y) + average)

# yAxis = list()
# for i in range(len(xAxis)-1):
#     yAxis.append(sum(x >= xAxis[i] and x < xAxis[i+1] for x in li))
# yAxis.append(sum(x >= xAxis[len(xAxis)-1] and x < 2 *
#                  xAxis[len(xAxis)-1]-xAxis[len(xAxis)-2] for x in li))

# plt.plot(xAxis, yAxis)
# plt.show()
