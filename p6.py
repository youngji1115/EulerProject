sumsquare = 0
squaresum = 0

for i in range(1,101):
        sumsquare += i
        squaresum += i**2

sumsquare = sumsquare**2

print sumsquare - squaresum
