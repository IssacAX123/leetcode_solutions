def guess(n):
    if n == 10:
        return 0
    elif n < 10:
        return 1
    elif n > 10:
        return -1


def guessNumber_issac(n: int) -> int:
    found = False
    left = 1
    right = n
    while not found:
        mid = (left + right) // 2
        result = guess(mid)
        if result == 0:
            found = True
            return mid
        elif result == 1:
            left = mid+1
        elif result == -1:
            right = mid-1

print(guessNumber_issac(20))