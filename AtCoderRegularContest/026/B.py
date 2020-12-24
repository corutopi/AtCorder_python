# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7


def divisor(x):
    """約数"""
    from math import floor
    re = []
    _x = floor(x ** 0.5)
    for i in range(1, _x + 1):
        if x % i == 0:
            re.append(i)
            if x // i != i:
                re.append(x // i)
    re.sort()
    return re


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    t = sum(divisor(N)[:-1])
    ans = ''
    if t == N:
        ans = 'Perfect'
    elif t > N:
        ans = 'Abundant'
    else:
        ans = 'Deficient'
    print(ans)



if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
