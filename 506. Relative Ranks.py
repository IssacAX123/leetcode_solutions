from typing import List


def findRelativeRanks_issac(score: List[int]) -> List[str]:
    my_dict = {i+1: 0 for i in score}
    new_array = sorted(score, reverse=True)
    result = []
    for i, key in enumerate(new_array):
        val = ""
        if i == 0:
            val = "Gold Medal"
        elif i == 1:
            val = "Silver Medal"
        elif i == 2:
            val = "Bronze Medal"
        else:
            val = str(i+1)

        my_dict[key] = val

    for val in score:
        result.append(my_dict[val])

    return result

print(findRelativeRanks_issac([10,3,8,9,4]))


