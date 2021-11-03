# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def binary_search(ok, ng, solve):
    """めぐる式2分探索"""
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


# from decorator import stop_watch
#
#
# @stop_watch
def solve(X, M):
    d = max((int(s) for s in X))
    if len(X) == 1:
        print(1 if int(X) <= M else 0)
        return

    def to10(s, base):
        # print(base, sum((int(x) * base ** i for i, x in enumerate(reversed(s)))))
        return sum((int(x) * base ** i for i, x in enumerate(reversed(s))))

    tmp = binary_search(0, 10 ** 19, lambda x: to10(X, x) <= M)

    print(max(0, tmp - d))


if __name__ == '__main__':
    # S = input()
    X = input()
    M = int(input())
    solve(X, M)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # X = str(random_str(60, '10'))
    # M = randint(1, 10 ** 18)
    # solve(X, M)
