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
def solve(N, L, a):
    key = 0
    for i in range(N - 1):
        if a[i] + a[i + 1] >= L:
            key = i
            break
    else:
        print('Impossible')
        return
    print('Possible')
    [print(i + 1) for i in range(key)]
    [print(i) for i in range(N - 1, key + 1, - 1)]
    print(key + 1)


if __name__ == '__main__':
    N, L = map(int, input().split())
    a = [int(i) for i in input().split()]
    solve(N, L, a)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
