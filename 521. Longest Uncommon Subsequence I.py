import collections


def findLUSlength(a: str, b: str) -> int:
    if a == b:
        return -1
    if len(a) == len(b):
        return len(a)
    if len(a) != len(b):
        return max(len(a),len(b))

print(findLUSlength("aaa", "aaa"))
