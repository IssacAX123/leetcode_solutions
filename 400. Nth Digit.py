# 1-------9 9*1 = 9 digits
# 10-----99 90 *2 = 180 digits
# 100---999 900 * 3 = 2700 digits
import math


def findNthDigit(n: int) -> int:
    digit_len = 1
    count = 9
    while n > count*digit_len:
        n -= count*digit_len
        digit_len += 1
        count *= 10

    start = (10 ** (digit_len-1))
    num, remaining = divmod(n, digit_len)
    if remaining == 0:
        return int(str(start + num - 1)[-1])  # number from 100 to 114 is actually 15 number
    else:
        return int(str(start + num)[remaining-1])

print(findNthDigit(11))
