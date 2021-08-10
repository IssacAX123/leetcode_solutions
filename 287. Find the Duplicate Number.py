from typing import List

#wrong but works
def findDuplicate_issac(nums: List[int]) -> int:
    n = len(nums)-1
    total = (n*(n+1))//2
    for num in nums:
        total -= num
    return abs(total)

def findDuplicate_online(nums: List[int]) -> int:
    slow = fast = finder = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            while finder != slow:
                finder = nums[finder]
                slow = nums[slow]
            return finder


print(findDuplicate_online([3, 1, 3, 4, 2]))