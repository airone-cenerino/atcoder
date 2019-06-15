import random
import math
import matplotlib.pyplot as plt

sampleNum = 1000
li = list()

print("Input average : ", end="")
average = int(input())
print("Input variance : ", end="")
variance = int(input())

for i in range(sampleNum):
    x = random.random()
    y = random.random()
    li.append(variance * math.sqrt(-2*math.log(x))
              * math.cos(2 * math.pi * y) + average)

plt.plot(li)
plt.show()
