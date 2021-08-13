from typing import List


def longestConsecutive(nums: List[int]) -> int:
    nums = set(nums)
    sequence_starts = []
    for n in nums:
        if n - 1 not in nums:
            sequence_starts.append(n)
    largest_sequence = 0
    for num in sequence_starts:
        seq_len = 1
        for i in range(num + 1, num + len(nums)):
            if i in nums:
                seq_len += 1
            else:
                break
        if seq_len > largest_sequence:
            largest_sequence = seq_len

    return largest_sequence

print(longestConsecutive([100,4,200,1,3,2]))
