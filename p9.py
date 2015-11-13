import math
r_a = 0
r_b = 0
r_c = 0

for a in range(1,999):
        for b in range(1,999):
                c = math.sqrt(a**2+b**2)
                d = int(c)
                if d**2 != (a**2+b**2):
                        continue
                if a+b+d == 1000:
                        r_a = a
                        r_b =b
                        r_c = d
                        break
        if r_a != 0:
                break

print r_a* r_b* r_c
~                     