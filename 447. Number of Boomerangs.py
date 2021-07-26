from typing import List
import math


def numberOfBoomerangs(points: List[List[int]]) -> int:
    def get_distance(point1, point2):
        return math.sqrt(((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2))

    if len(points) < 3:
        return 0
    my_dict = {}
    boomerang = 0
    for i in points:
        for j in points:
            if i != j:
                distance = get_distance(i, j)
                if distance in my_dict:
                    my_dict[distance] += 1
                else:
                    my_dict[distance] = 1
        for k, v in my_dict.items():
            boomerang += v * (
                        v - 1)  # permutation formula simplified by factor cancellation and taking res as 2 or more
        my_dict.clear()
    return boomerang


print(numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))
