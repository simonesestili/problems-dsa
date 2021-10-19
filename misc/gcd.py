def gcd(x, y):
    x, y = min(x, y), max(x, y)
    if not x:
        return y
    return gcd(y % x, x)
