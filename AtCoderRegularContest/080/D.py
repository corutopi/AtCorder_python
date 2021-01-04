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
def solve(H, W, a):
    ans = [[0] * W for _ in range(H)]
    i = 0
    a_count = 0
    for h in range(H):
        r = range(W) if h % 2 == 0 else reversed(range(W))
        for w in r:
            ans[h][w] = i + 1
            a_count += 1
            if a[i] == a_count:
                i += 1
                a_count = 0
    [print(' '.join([str(ans_hw) for ans_hw in ans_h])) for ans_h in ans]


if __name__ == '__main__':
    H, W = map(int, input().split())
    N = int(input())
    a = [int(i) for i in input().split()]
    solve(H, W, a)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
