import collections


def firstUniqChar_issac(s: str) -> int:
    count_map  = {}
    index_map = {}
    for i, c in enumerate(s):
        if c in count_map:
            count_map[c] += 1
            if c in index_map:
                del index_map[c]
        else:
            count_map[c] = 1
            index_map[c] = i
    if len(index_map) == 0:
        return -1
    else:
        min = (10**5) - 1
        for char, i in index_map.items():
            if i < min:
                min = i
        return min

def firstUniqChar_online(s: str) -> int:
    count = collections.Counter(s)

    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    return -1

print(firstUniqChar_issac("aadadaad"))
