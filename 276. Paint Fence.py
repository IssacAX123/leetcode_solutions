def paintFence(n: int, k: int) -> int:
    if k == 0 or n == 0:
        return 0
    if n == 1:
        return k

    same = k
    diff = k * (k - 1)
    for _ in range(3, n + 1):
        tmp = same
        same = diff
        diff = (tmp + diff) * (k-1)

    return same + diff

print(paintFence(3, 2))