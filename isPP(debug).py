def isPP(n):
    import itertools
    power = itertools.count(2)
    for m in range(2, n-1):
        for k in itertools.count(2):
            if m**k == n:
                return [m, k]
            elif m**k > n:
                break
    return [None]          