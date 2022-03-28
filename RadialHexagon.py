def radialHexagons(t, n, length):
    for count in range(n):
        hexagon(t,length)
        t.left(360 / n)

