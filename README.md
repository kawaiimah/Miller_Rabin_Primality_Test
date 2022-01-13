# Miller_Rabin_Primality_Test
Was exploring the [Miller-Rabin Primality Test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) and thought to give it a go at coding it up. Strictly speaking, the primality test that I ultimately implemented is a deterministic Miller test for numbers up to 3,825,123,056,546,413,051 with turnaround time of well less than a second.

## Coding Concepts
- Included time.perf_counter to check how long it takes to conduct the test
- Included a number generator to create random 15-digit numbers to test
- Included standard 'brute force' algorithm for comparison (took a bit of shortcut in terms of having a pre-generated list of prime numbers in primes.txt)

## Notes
Also did up a separate testing program to collect some stats. From a couple of runs of 1000 15-digit numbers (that are not even, not multiples of 5 and not multiples of 3), some observations as follows:
- ~11% of such 15-digit numbers turn out to be primes
- The Miller test was faster ~37% of the time.
- Note that the brute force test is sometimes faster simply because the number to be tested is divisible by a small prime like 7. Also note that I used a pre-generated list of primes to save time. Included in the code is a commented snippet that conducts the brute force test on the fly - testing large numbers will take exceedingly long for large primes.

## Addendum
Turns out the primes.txt file is too large to upload, I had to split it to 3 files. Pls join them up manually or otherwise edit the code a bit to make use of them.
