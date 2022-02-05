# 解説AC
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
def solve(H, W, K, A, B):
    if sum(A) % K != sum(B) % K:
        print(-1)
        return

    C = [((K - 1) * W) % K - a for a in A]
    C = [c + (K if c < 0 else 0) for c in C]
    D = [((K - 1) * H) % K - b for b in B]
    D = [d + (K if d < 0 else 0) for d in D]
    print(H * W * (K - 1) - max(sum(C), sum(D)))


if __name__ == '__main__':
    H, W, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    solve(H, W, K, A, B)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
