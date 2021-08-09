from typing import List
from collections import Counter


def containsDuplicate_issac(nums: List[int]) -> bool:
    counter = Counter(nums)
    print(counter)
    for key in counter:
        if counter[key] != 1:
            return True
    return False

def containsDuplicate_online(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False

print(containsDuplicate_online([1, 2, 3, 1]))
