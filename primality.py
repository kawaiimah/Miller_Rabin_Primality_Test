# -*- coding: utf-8 -*-
"""
Miller-Rabin Primality Test
"""

from time import perf_counter as pc

# Input number
nn = input('Number to test? ')

# Option for random number
if nn == '':
    from random import choice as ch
    for i in range(14):
        nn += ch('1234567890')
    nn += ch('1379')
    print(f'Randomly generated number = {nn}')

# Check if input is integer
n = int(nn)

# Check if even or multiple of 5 or multiple of 3
if nn[-1] in '24680':
    print('Even number')
elif nn[-1] == '5':
    print('Multiple of 5')
elif sum([int(c) for c in nn]) % 3 == 0:
    print('Multiple of 3')

# Miller-Rabin Test
else:
    start = pc()
    
    a = []
    if n < 1373653:
        a = [2,3]
    elif n < 25326001:
        a = [2,3,5]
    elif n < 3215031751:
        a = [2,3,5,7]
    elif n < 2152302898747:
        a = [2,3,5,7,11]
    elif n < 3474749660383:
        a = [2,3,5,7,11,13]
    elif n < 341550071728321:
        a = [2,3,5,7,11,13,17]
    elif n < 3825123056546413051:
        a = [2,3,5,7,11,13,17,19,23]
        
    if a:
        d = int(n - 1)
        r = 0
        while d % 2 == 0:
            d = d // 2
            r += 1
            
        prime = True
        for i in a:
            x = pow(i,d,n)
            if x == 1 or x == n-1:
                continue
            else:
                prime = False
                if r == 1:
                    break
                for j in range(r-1):
                   x = pow(x,2,n)
                   if x == n-1:
                       prime = True
                       break
            if not prime:
                break
            
        end = pc()
        if prime:
            print('Miller-Rabin Test: Prime')
        else:
            print('Miller-Rabin Test: Not prime')
        print(f'Time elapsed (s): {end-start:.8f}')
        
        # Brute force test if n is not too big
        if n < 9999997800000121:
            print('')
            print('Reading in primes.txt for brute force test')
            known = []
            with open('primes.txt','r') as f:
                for row in f:
                    known.append(int(row.replace('\n','')))
    
            start = pc()
            prime = True
            for i,p in enumerate(known):
                if p*p > n:
                    break
                if n % p == 0:
                    prime = False
                    factor = p
                    break
                if i % 100000 == 0 and i > 0:
                    print(f'{i} prime factors tested...')
            end = pc()
            if prime:
                print('Brute force test: Prime')
            else:
                print(f'Brute force test: Not prime, first prime factor = {factor}')
            print(f'Time elapsed (s): {end-start:.8f}')        
    
    else:
        print('Sorry that is too large!')

# def isprime(x):
#     global known
#     out = True
#     f = 0
#     if x in known:
#         return out,f
#     for i in range(3,x,2):
#         if i*i > x:
#             break
#         flag,factor = isprime(i)
#         if flag:
#             if x % i == 0:
#                 out = False
#                 f = i
#                 break
#     if out:
#         known.append(x)
#         print(f'New prime {x} added to known!')
#     return out,f