# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(n, m, d):
    x = (n - d) * 2 if d != 0 else n
    ans = x * (m - 1) / pow(n, 2)
    # print('%.10f' % (x * (m - 1) / pow(n, 2)))
    print(f'{ans:.10}')
    pass


if __name__ == '__main__':
    n, m, d = map(int, input().split())
    solve(n, m, d)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
