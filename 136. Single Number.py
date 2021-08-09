from typing import List


def singleNumber_issac(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res

print(singleNumber_issac([4,1,2,1,2]))