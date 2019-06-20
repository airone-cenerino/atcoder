import random
import math


def square(num):
    return num*num


sampleNum = 100


li = list()

print("Input average : ", end="")
average = int(input())
print("Input variance : ", end="")
variance = int(input())

for i in range(sampleNum):
    x = random.random()
    y = random.random()
    li.append(math.sqrt(variance * -2 * math.log(x))
              * math.cos(2 * math.pi * y) + average)

actuallyAverage = float(sum(li)) / sampleNum
li = list(map(square, li))
actuallySquareAverage = float(sum(li)) / sampleNum
actuallyVariance = actuallySquareAverage - actuallyAverage ** 2
print(actuallyVariance)
