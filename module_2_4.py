numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    p = 0
    for j in range (1, i+1):
        if i%j == 0:
            p+=1
        else:
            p+=0
    if p == 2:
        primes.append(i)
    elif p == 1:
        continue
    else:
        not_primes.append(i)
print (primes)
print(not_primes)