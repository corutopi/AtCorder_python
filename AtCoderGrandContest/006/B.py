# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

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
def solve(N, x):
    size = N * 2 - 1
    if x == 1 or x == size:
        print('No')
        return
    print('Yes')
    used = [0] * (size + 1)
    ans = [0] * size
    used[x] = 1
    ans[size // 2] = x
    used[1] = 1
    ans[size // 2 - 1] = 1
    used[size] = 1
    ans[size // 2 + 1] = size
    if x > 2:
        used[2] = 1
        ans[size // 2 + 2] = 2
    elif x < size - 1:
        used[size - 1] = 1
        ans[size // 2 - 2] = size - 1
    u = 1
    for i in range(size):
        if ans[i] != 0: continue
        while used[u] == 1:
            u += 1
        used[u] = 1
        ans[i] = u
    [print(a) for a in ans]


if __name__ == '__main__':
    N, x = map(int, input().split())
    solve(N, x)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
