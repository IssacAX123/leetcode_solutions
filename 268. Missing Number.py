from functools import reduce
from typing import List


def missingNumber_issac(nums: List[int]):
    n = len(nums)
    total = reduce(lambda x, y: x+y, [x for x in range(n+1)])
    for num in nums:
        total -= num
    return total

#faster but same concept as above
def missingNumber_online(nums: List[int]):
    res = len(nums)
    for i in range(len(nums)):
        res += i-nums[i]
    return res


#can also xor

print(missingNumber_issac([9, 6, 4, 2, 3, 5, 7, 0, 1]))
