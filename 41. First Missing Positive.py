from typing import List

def firstMissingPositive(nums: List[int]) -> int:
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = 0

    for n in nums:
        index = abs(n)-1
        if 0 <= index < len(nums):
            if nums[index] > 0:
                nums[index] = -abs(nums[index])
            elif nums[index] == 0:
                nums[index] = -1 * (len(nums)+1)

    for n in range(1, len(nums)+1):
        if nums[n-1] >= 0:
            return n
    return len(nums)+1

print(firstMissingPositive([3,4,-1,1]))
