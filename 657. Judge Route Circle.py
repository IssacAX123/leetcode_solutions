def judgeCircle_issac(moves: str) -> bool:
    coords = [0, 0]
    for move in moves:
        coords = move_func(coords, move)
    return coords == [0, 0]

def move_func(coords, move):
    if move == "U":
        coords[1] += 1
    elif move == "D":
        coords[1] += -1
    elif move == "L":
        coords[0] += -1
    elif move == "R":
        coords[0] += 1
    return coords

print(judgeCircle_issac("LL"))