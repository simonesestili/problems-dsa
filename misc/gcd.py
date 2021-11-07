def gcd(x, y):
    if not x:
        return y
    return gcd(y % x, x)
