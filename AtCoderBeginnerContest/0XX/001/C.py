# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(Deg, Dis):
    Deg = int(Deg * 10)
    wind_angle = [1125 + 2250 * i for i in range(16)]
    wind_mark = ['NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S',
                 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N']
    mark = wind_mark[-1]
    for i in range(len(wind_angle) - 1):
        if wind_angle[i] <= Deg < wind_angle[i + 1]:
            mark = wind_mark[i]
            break

    from decimal import Decimal, ROUND_HALF_UP
    Dis = Decimal(Dis * 10 / 60).quantize(Decimal(0), rounding=ROUND_HALF_UP)
    wind_speed = [0, 3, 16, 34, 55, 80, 108, 139, 172, 208, 245, 285, 327, inf]
    # wind_power = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    power = 0
    for i in range(len(wind_speed)):
        if wind_speed[i] <= Dis:
            power = i
    if power == 0:
        mark = 'C'
    print(mark, power)


if __name__ == '__main__':
    Deg, Dis = map(float, input().split())
    solve(Deg, Dis)

    # # test
    # from random import randint
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
