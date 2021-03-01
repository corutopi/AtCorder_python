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
    tenjo = int(N ** 0.5) + 1
    visited = [0] * (tenjo + 1)
    can = 0
    for a in range(2, tenjo):
        if visited[a] == 1:
            continue
        b = 2
        while True:
            x = a ** b
            if x > N:
                break
            if x <= tenjo:
                visited[x] = 1
            b += 1
        can += b - 2
    print(N - can)


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
