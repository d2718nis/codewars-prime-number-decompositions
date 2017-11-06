def get_all_prime_factors(n):
    """Get prime decomposition by ascending factors for the given number.

    Keyword arguments:
    n -- integer value to get prime decomposition for

    Return a list of prime factors, sorted by ascending order, e.g.:
    [2, 2, 5, 5].
    """
    if type(n) is not int or n < 1:
        # Not an integer, negative or 0
        return []
    elif n < 3:
        return [n]
    factors = []
    while n > 1:
        for i in range(2, n+1):
            if is_prime(i) and not n % i:
                factors.append(i)
                n = int(n/i)
                break
    return factors

def get_unique_prime_factors_with_count(n):
    """Get a list containing two lists: one with prime numbers appearing in the
    decomposition and the other containing their respective power.

    Keyword arguments:
    n -- integer value to get the lists for

    Return a list of two lists, e.g.: [[2,5],[2,2]].
    """
    f = get_all_prime_factors(n)
    factors = list(set(f))
    powers = [f.count(factor) for factor in factors]
    return [factors, powers]

def get_unique_prime_factors_with_products(n):
    """Get a list of prime factors raised to the power of their respective
    powers.

    Keyword arguments:
    n -- integer value to get the list for

    Return a list, e.g.: [4,25].
    """
    cf = get_unique_prime_factors_with_count(n)
    return [factor**count for factor, count in zip(cf[0], cf[1])]

def is_prime(n):
    """Check if given number is a prime number.

    Keyword arguments:
    n -- integer value to check if it is a prime number

    Return True is the number is prime, otherwise False.
    """
    for i in range(2, n):
        if not n % i:
            return False
    return True
