def liner_function(x1, y1, x2, y2):
    """return a, b, c of ax + by + c = 0.
    b = 0 or 1
    x1 != x2 or y1 != y2
    :param x1: meet y1 = ax1 + b
    :param y1:
    :param x2: meet y2 = ax2 + b
    :param y2:
    :return:
    """
    if x1 == x2:
        a = 1
        b = 0
        c = - x1
    elif y1 == y2:
        a = 0
        b = 1
        c = - y1
    else:
        b = 1
        a = - (y1 - y2) / (x1 - x2)
        c = - a * x1 - b * y1
    return a, b, c


def vertical_line(a, b, c, x, y):
    """retrun a1, b1, c1 of 'a1x + b1y + c = 0' intersect 'ax + by + c = 0' vertically.

    :param a:
    :param b:
    :param c:
    :param x:
    :param y:
    :return:
    """
    if a == 0:
        a1 = 1
        b1 = 0
        c1 = - x
    elif b == 0:
        a1 = 0
        b1 = 1
        c1 = - y
    else:
        a, b, c = a / b, b / b, c / b
        b1 = 1
        a1 = -  1 / a
        c1 = - (a1 * x) - (b1 * y)
    return a1, b1, c1


def liner_cross_point(a1, b1, c1, a2, b2, c2):
    """return x, y of cross two line 'a1x + b1y + c1 = 0' and 'a2x + b2y + c2 = 0'.

    :param a1:
    :param b1:
    :param c1:
    :param a2:
    :param b2:
    :param c2:
    :return:
    """
    if a1 == 0 or a2 == 0:
        if a2 == 0:
            a1, b1, c1, a2, b2, c2 = a2, b2, c2, a1, b1, c1
        y = - c1 / b1
        x = - (b2 * y + c2) / a2
    elif b1 == 0 or b2 == 0:
        if b2 == 0:
            a1, b1, c1, a2, b2, c2 = a2, b2, c2, a1, b1, c1
        x = - c1 / a1
        y = - (a2 * x + c2) / b2
    else:
        a1, b1, c1 = a1 / b1, b1 / b1, c1 / b1
        a2, b2, c2 = a2 / b2, b2 / b2, c2 / b2
        x = - (c1 - c2) / (a1 - a2)
        y = - a1 * x - c1
    return x, y


def binary_search(ok, ng, solve):
    """めぐる式2分探索"""
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


class Coordinate:
    """a class that manipulates 2D coordinates(x, y)
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotation_right(self, degree, center_x=0, center_y=0):
        from math import sin, cos, radians
        r = radians(degree)
        R = [[cos(r), -sin(r)],
             [sin(r), cos(r)]]
        self.x, self.y = self.x - center_x, self.y - center_y
        self.x, self.y = R[0][0] * self.x + R[0][1] * self.y, \
                         R[1][0] * self.x + R[1][1] * self.y
        self.x, self.y = self.x + center_x, self.y + center_y

