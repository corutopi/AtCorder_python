# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    ans = 0
    N = '00' + N
    x = 0
    O = list(map(int, reversed(N)))
    for i in range(len(O) - 1):
        s = O[i]
        if s + x < 5 or (s + x == 5 and O[i + 1] < 5):
            ans += s + x
            x = 0
        else:
            ans += 10 - (s + x)
            x = 1
    print(ans)
    # return ans


def solve_force(N):
    ans = inf
    for i in range(N, N * 10):
        a, b = i, i - N
        tmp = 0
        while a > 0:
            a, x = divmod(a, 10)
            tmp += x
        while b > 0:
            b, x = divmod(b, 10)
            tmp += x
        ans = min(ans, tmp)
    return ans


if __name__ == '__main__':
    N = input()
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # solve(random_str(10 ** 6, '0123456789'))
    # # print(solve(str(65)))

    # for i in range(1, 1000):
    #     if solve_force(i) != solve(str(i)):
    #         print(i, solve_force(i), solve(str(i)))
    #         break
