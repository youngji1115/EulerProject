largest_palindrome = 0

for i in range (100,1000):
        for j in range (100,1000):
                multiple = i*j
                if multiple/100000 != 0:  #6-digit
                        tmp1 = multiple%100000
                        tmp2 = multiple%100
                        if multiple/100000 == multiple%10 and tmp1/10000 == tmp2/10:
                                tmp1 = multiple%10000
                                tmp2 = multiple%1000
                                if tmp1/1000 == tmp2/100:
                                        if largest_palindrome < multiple:
                                                largest_palindrome = multiple

print largest_palindrome