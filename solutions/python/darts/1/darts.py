def score(x, y):
    if (distanceFromOrigin(x, y)) > 10:
        return 0
    if 5 < distanceFromOrigin(x, y) <= 10:
        return 1
    if 1 < distanceFromOrigin(x, y) <= 5:
        return 5
    if distanceFromOrigin(x, y) <= 1:
        return 10
    return None
def distanceFromOrigin(x, y):
    return (x * x + y * y) ** 0.5