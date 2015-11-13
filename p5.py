smallest_n = 1

for i in range(2,21):
        temp = 0
        for j in range(2,i):
                if i%j == 0 and j!= i:
                        temp = 1
                        break
        if temp == 0:
                smallest_n *= i

smallest_n *= 24

print smallest_n
