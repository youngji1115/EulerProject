fibonacci = [1,2]

for i in range(0,2000):
        if fibonacci[i]+fibonacci[i+1] > 4000000:
                break
        fibonacci.append(fibonacci[i]+fibonacci[i+1])

even_sum = 0

for i in fibonacci:
        if i%2==0:
                even_sum += i

print even_sum