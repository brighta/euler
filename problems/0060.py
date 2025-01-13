from math import floor, sqrt

def is_prime(number_to_check):
    for divisor in range(floor(sqrt(number_to_check)), 1, -1):
        if number_to_check % divisor == 0:
            return False
    return True

def get_next_prime():
    global primes
    next_prime_candidate = primes[-1] + 2
    while not is_prime(next_prime_candidate):
        next_prime_candidate += 2
    primes.append(next_prime_candidate)

def is_prime_pair(prime_1, prime_2):
    prime_1_str = str(prime_1)
    prime_2_str = str(prime_2)
    return is_prime(int(prime_1_str + prime_2_str)) and is_prime(int(prime_2_str + prime_1_str))

primes = [2, 3]
while primes[-1] < 10000:
    get_next_prime()
for a in range(len(primes)):
    prime_a = primes[a]
    for b in range(prime_a + 1, len(primes)):
        prime_b = primes[b]
        if is_prime_pair(prime_a, prime_b):
            for c in range(b + 1, len(primes)):
                prime_c = primes[c]
                if is_prime_pair(prime_a, prime_c) and is_prime_pair(prime_b, prime_c):
                    for d in range(c + 1, len(primes)):
                        prime_d = primes[d]
                        if is_prime_pair(prime_a, prime_d) and is_prime_pair(prime_b, prime_d) and is_prime_pair(prime_c, prime_d):
                            for e in range(d + 1, len(primes)):
                                prime_e = primes[e]
                                if is_prime_pair(prime_a, prime_e) and is_prime_pair(prime_b, prime_e) and is_prime_pair(prime_c, prime_e) and is_prime_pair(prime_d, prime_e):
                                    print(prime_a + prime_b + prime_c + prime_d + prime_e)
                                    exit()
