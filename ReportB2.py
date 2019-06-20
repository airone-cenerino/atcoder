import random
import math

sampleNum = 100

print("Input average : ", end="")
average = int(input())
print("Input variance : ", end="")
variance = int(input())

for i in range(sampleNum):
    x = random.random()
    y = random.random()
    print(variance * math.sqrt(-2*math.log(x))
          * math.cos(2 * math.pi * y) + average)
