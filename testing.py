# -*- coding: utf-8 -*-
"""
Testing program for
Miller-Rabin Primality Test
"""

from time import perf_counter as pc
from random import choice as ch

print('\nReading in primes.txt for brute force test\n')
known = []
with open('primes.txt','r') as f:
    for row in f:
        known.append(int(row.replace('\n','')))
testn = []
mr = []
mrtime = []
bf = []
bftime = []
count = []
primefactors = []
cycles = 1000
for z in range(cycles):
    
    while True:
        nn = ch('123456789')
        for i in range(13):
            nn += ch('1234567890')
        nn += ch('1379')
        if sum([int(c) for c in nn]) % 3 != 0:
            print(f'{z}: Randomly generated number = {nn}')
            n = int(nn)
            testn.append(n)
            break
    
    # Miller-Rabin Test
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
        mrtest = prime
        mr.append(mrtest)
        mrtime.append(f'{end-start:.8f}')
        
        # Brute force test if n is not too big
        if n < 9999997800000121:        
            start = pc()
            prime = True
            for i,p in enumerate(known):
                if p*p > n:
                    break
                if n % p == 0:
                    prime = False
                    factor = p
                    break
            end = pc()
            bftest = prime
            bf.append(bftest)
            bftime.append(f'{end-start:.8f}')    

            count.append(mrtest==bftest)
            if prime:
                primefactors.append(n)
            else:
                primefactors.append(factor)

isprime = []
mr_faster = []
factor = []
prime = []
for x,y in zip(mr,primefactors):
    if x:
        isprime.append(1)
        prime.append(y)
        factor.append(0)
    else:
        isprime.append(0)
        prime.append(0)
        factor.append(y)
for x,y in zip(mrtime,bftime):
    if x < y:
        mr_faster.append(1)
    else:
        mr_faster.append(0)

with open('out.txt','w') as f:
    f.write('testn,mr,mrtime,bf,bftime,count,primefactors,isprime,mr_faster,factor,prime\n')
    for x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11 in zip(testn,mr,mrtime,bf,bftime,count,primefactors,isprime,mr_faster,factor,prime):
        f.write(f'{x1},{x2},{x3},{x4},{x5},{x6},{x7},{x8},{x9},{x10},{x11}\n')