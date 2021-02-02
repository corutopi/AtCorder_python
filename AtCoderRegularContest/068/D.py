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
def solve(N, A):
    number = [0] * (10 ** 5 + 1)
    dbl = 0
    for a in A:
        if number[a] == 0:
            number[a] += 1
        else:
            dbl += 1
    ans = sum(number)
    if dbl % 2 == 1:
        ans -= 1
    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
