from typing import List


def findMaxConsecutiveOnes_issac(nums: List[int]) -> int:
    max = 0
    count = 0
    for i in nums:
        if i == 1:
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    if count > max:
        max = count
    return max

print(findMaxConsecutiveOnes_issac([1, 1, 0, 1, 1, 1]))
