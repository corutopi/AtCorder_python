"""
A - Still TBD
"""

from datetime import datetime as dt


def solve():
    target_day = dt.strptime(input(), '%Y/%m/%d')
    limit_day = dt(2019, 4, 30)
    if target_day > limit_day:
        print('TBD')
    else:
        print('Heisei')


if __name__ == '__main__':
    solve()
