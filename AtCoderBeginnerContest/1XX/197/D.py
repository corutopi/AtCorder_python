# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


class Coordinate:
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


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, x0, y0, xN2, yN2):
    cx, cy = (x0 + xN2) / 2, (y0 + yN2) / 2
    cd = Coordinate(x0, y0)
    cd.rotation_right(360 / N, cx, cy)
    print(cd.x, cd.y)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    solve(N, x0, y0, xN2, yN2)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
