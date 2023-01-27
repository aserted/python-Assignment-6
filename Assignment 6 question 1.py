def is_perfect(n):
    divisors = [x for x in range(1, n) if n % x == 0]
    if sum(divisors) == n:
        return True
    else:
        return False
