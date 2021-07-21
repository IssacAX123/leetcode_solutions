def isPowerOfTwo_issac(n: int) -> bool:
    while n >= 2:
        if n % 2 != 0:
            return False
        n = n/2
    return n == 1

print(isPowerOfTwo_issac(0))