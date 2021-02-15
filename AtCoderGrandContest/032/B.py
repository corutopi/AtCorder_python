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
    key = N + 1 if N % 2 == 0 else N
    ans = []
    for i, j in ((i, j) for i in range(1, N) for j in range(i + 1, N + 1)):
        if i + j == key: continue
        ans.append((str(i), str(j)))
    print(len(ans))
    [print(' '.join(a)) for a in ans]


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
