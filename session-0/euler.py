import math

# Multiples of 3 or 5
def euler_1(limit=1000):
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)
# Time: O(n), Space: O(1)

# Even Fibonacci numbers
def euler_2(limit=4000000):
    a, b = 1, 2
    total = 0
    while b <= limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total
# Time: O(n), Space: O(1)

# Largest prime factor
def euler_3(n=600851475143):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n
# Time: O(sqrt(n)), Space: O(1)

# Largest palindrome product
def euler_4():
    max_pal = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            prod = i * j
            if str(prod) == str(prod)[::-1] and prod > max_pal:
                max_pal = prod
    return max_pal
# Time: O(n^2), Space: O(1)

# Smallest multiple
def euler_5(n=20):
    def lcm(a, b):
        return a * b // math.gcd(a, b)
    res = 1
    for i in range(2, n+1):
        res = lcm(res, i)
    return res
# Time: O(n log n), Space: O(1)

# Sum square difference
def euler_6(n=100):
    sum_sq = sum(i*i for i in range(1, n+1))
    sq_sum = sum(range(1, n+1)) ** 2
    return sq_sum - sum_sq
# Time: O(n), Space: O(1)

# 10001st prime
def euler_7(n=10001):
    primes = []
    candidate = 2
    while len(primes) < n:
        for p in primes:
            if candidate % p == 0:
                break
        else:
            primes.append(candidate)
        candidate += 1
    return primes[-1]
# Time: O(n sqrt(n)), Space: O(n)

# Largest product in a series
def euler_8(series, k=13):
    digits = [int(d) for d in series if d.isdigit()]
    max_prod = 0
    for i in range(len(digits) - k + 1):
        prod = 1
        for j in range(k):
            prod *= digits[i + j]
        if prod > max_prod:
            max_prod = prod
    return max_prod
# Time: O(n*k), Space: O(n)

# Special Pythagorean triplet
def euler_9(total=1000):
    for a in range(1, total//3):
        for b in range(a+1, total//2):
            c = total - a - b
            if a*a + b*b == c*c:
                return a * b * c
# Time: O(n^2), Space: O(1)

# Summation of primes
def euler_10(limit=2000000):
    sieve = [True] * limit
    sieve[0:2] = [False, False]
    for i in range(2, int(limit**0.5)+1):
        if sieve[i]:
            sieve[i*i:limit:i] = [False] * len(range(i*i, limit, i))
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)
# Time: O(n log log n), Space: O(n)