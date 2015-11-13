number = 600851475143

for i in xrange(2,number):
        while (number%i)==0:
                number /= i
        if number == 1:
                break

print i