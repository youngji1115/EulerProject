import math
primesum = 0
prime = [2]

for i in range(3,2000000):
        temp = 0
        sqr = math.sqrt(i)
        for j in prime:
                if j > sqr:
                        break
                if i%j == 0:
                        temp = 1
                        break
        if temp == 0 :
                prime.append(i)

for i in prime:
        primesum += i

print primesum
