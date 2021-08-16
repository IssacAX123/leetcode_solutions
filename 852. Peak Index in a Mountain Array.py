from typing import List

# n but les space
def peakIndexInMountainArray_issac(arr: List[int]) -> int:
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
            return i


# log n but more space
def peakIndexInMountainArray_online(arr: List[int]) -> int:
    lp, rp = 0, len(arr) - 1
    while True:  # loops forever since there will be always be a peak in the test case:
        i = (lp + rp) // 2
        if arr[i - 1] < arr[i] > arr[i + 1]:
            return i
        elif arr[i - 1] < arr[i] < arr[i + 1]:
            lp = i + 1
        elif arr[i - 1] > arr[i] > arr[i + 1]:
            rp = i - 1

