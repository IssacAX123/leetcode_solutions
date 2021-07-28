from math import ceil


def repeatedStringMatch_online(a: str, b: str) -> int:
    times = ceil(len(b) / len(a)) + 1
    c = a * times
    if b not in c:
        return -1
    while b in a * (times - 1):
        times -= 1
    return times


