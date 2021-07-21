def isPowerOfThree_issac(n: int) -> bool:
    if n == 1:
        return True
    while True:
        if n % 3 == 0:
            n /= 3
            if n == 1:
                return True
            if n < 1:
                return False
        else:
            return False

def isPowerOfThree_online(n: int) -> bool:
    while n >= 3:
        if n % 3 != 0:
            return False
        n = n/3
    return n == 1

print(isPowerOfThree_issac(0))