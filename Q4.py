import math

def entropy(y):
    n = len(y)
    if n == 0:
        return 0.0

    freq = {}
    for lbl in y:
        freq[lbl] = freq.get(lbl, 0) + 1

    if len(freq) == 1:
        return 0.0

    H = 0
    for c in freq.values():
        p = c / n
        H -= p * math.log2(p)

    return round(H, 4)
