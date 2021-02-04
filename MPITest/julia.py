c = complex(0, 0.65)


def julia(x, y):
    z = complex(x, y)
    n = 255
    while abs(z) < 3 and n > 1:
        z = z**2 + c
        n -= 1
    return n


def julia_line(args):
    k, w, h = args
    x0, x1 = -2.0, +2.0
    y0, y1 = -1.5, +1.5
    dx = (x1 - x0) / w
    dy = (y1 - y0) / h

    line = bytearray(w)
    y = y1 - k * dy
    for j in range(w):
        x = x0 + j * dx
        line[j] = julia(x, y)
    return line
