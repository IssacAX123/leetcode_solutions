from typing import List


def findDuplicates(nums: List[int]):
    result = []
    for n in nums:
        i = abs(n) - 1
        if nums[i] < 0:
            result.append(i+1)
        else:
            nums[i] = -1 * abs(nums[i])
    return result


print(findDuplicates([1]))