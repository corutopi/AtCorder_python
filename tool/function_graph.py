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
        # y軸に平行な直線の場合
        a = 1
        b = 0
        c = - x1
    elif y1 == y2:
        # x軸に平行な直線の場合
        a = 0
        b = 1
        c = - y1
    else:
        b = 1
        a = - (y1 - y2) / (x1 - x2)
        c = - a * x1 - b * y1
    return a, b, c


def liner_function_integer(x1, y1, x2, y2):
    """return a, b, c of ax + by + c = 0.
    a, b and c are relatively prime integers. a >= 0.
    x1 != x2 or y1 != y2
    :param x1: meet y1 = ax1 + b
    :param y1:
    :param x2: meet y2 = ax2 + b
    :param y2:
    :return:
    """

    def gcd(a, b):
        """最大公約数"""
        a, b = (a, b) if a >= b else (b, a)
        if b == 0:
            return a
        return gcd(b, a % b)

    if x1 == x2:
        # y軸に平行な直線の場合
        a = 1
        b = 0
        c = - x1
    elif y1 == y2:
        # x軸に平行な直線の場合
        a = 0
        b = 1
        c = - y1
    else:
        b = 1 * (x1 - x2)
        a = - (y1 - y2)
        c = - a * x1 - b * y1
        g = gcd(gcd(abs(a), abs(b)), abs(c))
        b //= g
        a //= g
        c //= g
        code = 1 if a > 0 else -1
        b *= code
        a *= code
        c *= code
    return a, b, c


def vertical_line(a, b, c, x, y):
    """retrun a1, b1, c1 of 'a1x + b1y + c = 0' intersect 'ax + by + c = 0' vertically.

    直線A(ax + by + c = 0)上の座標(x, y)を通り,
    直線Aに対して垂直な直線B(a1x + b1x + c1 = 0)を表す a1, b1, c1 を返す.

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


def angle(ax, ay, bx, by, cx, cy):
    """return angle ∠abc degrees(0 to 180).

    :param ax:
    :param ay:
    :param bx:
    :param by:
    :param cx:
    :param cy:
    :return:
    """
    import math

    m1, m2 = ax - bx, ay - by
    n1, n2 = cx - bx, cy - by
    cos = (m1 * n1 + m2 * n2) / ((m1 ** 2 + m2 ** 2) ** 0.5 *
                                 (n1 ** 2 + n2 ** 2) ** 0.5)
    return math.degrees(math.acos(cos))


class Coordinate:
    """a class that manipulates 2D coordinates(x, y)
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotation_right(self, degree, center_x=0, center_y=0):
        """rotate n degrees right around (center_x, center_y).

        :param degree:
        :param center_x:
        :param center_y:
        :return:
        """
        from math import sin, cos, radians
        r = radians(degree)
        R = [[cos(r), -sin(r)],
             [sin(r), cos(r)]]
        self.x, self.y = self.x - center_x, self.y - center_y
        self.x, self.y = R[0][0] * self.x + R[0][1] * self.y, \
                         R[1][0] * self.x + R[1][1] * self.y
        self.x, self.y = self.x + center_x, self.y + center_y


def declination(x, y, center_x=0, center_y=0):
    """偏角"""
    from math import atan2, degrees
    return degrees(atan2(y - center_y, x - center_x)) % 360


def circle_coordinate(r, angle, x=0, y=0, ):
    """x, y を中心とする半径 r の円周上にあり, x 軸に水平な直線から angle 度だけ反時計回りに進んだ位置にある座標(m, n)を返す.
    より具体的には以下の条件に当てはまる座標(m, n)を返す.
        - 座標 x, y を中心座標とする半径 r の円周上にある.
        - 中心座標と座標(x + r, y)を結ぶ線分Aと, 中心座標と座標(m,n)のを結ぶ線分Bのなす角度が angle となる.
            - 角度は線分Aから反時計回り方向の角度を指定する.

    :param x:
    :param y:
    :param r:
    :param angle:
    :return:
    """
    from math import sin, cos, radians
    angle = angle % 360
    return cos(radians(angle)) * r + x, sin(radians(angle)) * r + y


def depression_angle_3d(x1, y1, z1, x2, y2, z2):
    """z軸を垂直方向とする3次元立面で座標1から見た時の座標2の俯角を返す.
    "俯角"を表すため, 座標2が座標1より上側にある場合, 角度は負になる.
    """
    from math import sqrt, degrees, atan
    c = sqrt((x1 - x2) ** 2 +
             (y1 - y2) ** 2 +
             (z1 - z2) ** 2)
    a = sqrt((z1 - z2) ** 2)
    b = sqrt((c ** 2) - (a ** 2))
    return degrees(atan(a / b)) * (1 if z1 >= z2 else -1)


def triangle_area(x1, y1, x2, y2, x3, y3):
    """座標(x1, y1), (x2, y2), (x3, y3) で表される三角形の面積.
    https://mathwords.net/x1y2hikux2y1
    """
    return abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) / 2
