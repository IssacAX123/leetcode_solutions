from typing import List


def readBinaryWatch_issac(turnedOn: int) -> List[str]:
    results = []
    for h in range(0, 12):
        for m in range(0, 60):
            if bin(h).count("1") + bin(m).count("1") == turnedOn:
                results.append(f"{h}:{m:02}")
    return results

print(readBinaryWatch_issac(1))