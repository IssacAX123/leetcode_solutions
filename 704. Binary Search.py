from typing import List


def search(nums: List[int], target: int) -> int:
    front = 0
    back = len(nums) - 1
    while front <= back:
        mid = (front + back) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            back = mid - 1
        elif target > nums[mid]:
            front = mid + 1
    return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
