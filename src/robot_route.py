def robot(n, m):
    route = []
    for row in range(1, m + 1):
        if row % 2 != 0:
            for i in range(1, n + 1):
                route.append((row - 1) * n + i)
        else:
            for i in range(n, 0, -1):
                route.append((row - 1) * n + i)

    return route
