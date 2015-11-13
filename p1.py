multiples_three_five = [i for i in range (1,1001) if (i%3)==0 or (i%5)==0]

sum = 0

for i in multiples_three_five:
	sum += i

print sum