prime = [2]
i = 3

while True:
        temp = 0
        for j in range(2,i):
                if i != j and i%j == 0:
                        temp = 1
                        break
        if temp == 0:
                prime.append(i)
        if len(prime)==10001:
                break
        i+=2

print prime[10000]
