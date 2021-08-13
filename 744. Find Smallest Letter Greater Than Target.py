from typing import List


def nextGreatestLetter(letters: List[str], target: str) -> str:
    # delas with the wrap
    if target >= letters[-1] or target < letters[0]:
        return letters[0]

    # gets the back pointer which will point to the next greatets element
    front = 0
    back = len(letters) - 1
    while front + 1 < back:
        mid = front + (back - front) // 2
        if letters[mid] <= target:
            front = mid
        else:
            back = mid
    return letters[back]

def online(letters, target):
    letters_length = len(letters)
    low = 0
    high = letters_length - 1

    # target is outside the bounds of letters
    # because the array is circular, this means that the next greatest value
    # must be the first value in the array. If the value is within the bounds
    # of the array we can perform our regular modified binary search
    if target < letters[low] or target >= letters[high]:
        return letters[low]

    while low <= high:
        middle = (low + high) // 2
        candidate = letters[middle]

        if target < candidate:
            high = middle - 1

        # becuase we're looking for the smallest value thats greater then the target
        # we can condense the typical case where target == letters[middle] into the
        # the target > letters[middle] case
        if target >= candidate:
            low = middle + 1

    return letters[low]
print(nextGreatestLetter(["c","f","j"], "j"))