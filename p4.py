{\rtf1\ansi\ansicpg949\deff0\deflang1033\deflangfe1042{\fonttbl{\f0\fnil\fcharset129 \'b8\'bc\'c0\'ba \'b0\'ed\'b5\'f1;}}
{\*\generator Msftedit 5.41.21.2510;}\viewkind4\uc1\pard\sa200\sl276\slmult1\lang18\f0\fs20 largest_palindrome = 0\par
\par
for i in range (100,1000):\par
        for j in range (100,1000):\par
                multiple = i*j\par
                if multiple/100000 != 0:  #6-digit\par
                        tmp1 = multiple%100000\par
                        tmp2 = multiple%100\par
                        if multiple/100000 == multiple%10 and tmp1/10000 == tmp2/10:\par
                                tmp1 = multiple%10000\par
                                tmp2 = multiple%1000\par
                                if tmp1/1000 == tmp2/100:\par
                                        if largest_palindrome < multiple:\par
                                                largest_palindrome = multiple\par
\par
print largest_palindrome\par
}
 