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
def solve(A, B, K):
    f = [1]
    for i in range(A + B):
        f.append(f[-1] * (i + 1))
    ans = ""
    for _ in range(A + B):
        border = f[A + B] // (f[A] * f[B]) * A // (A + B)
        if border >= K:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            B -= 1
            K -= border
    print(ans)




if __name__ == '__main__':
    A, B, K = map(int, input().split())
    solve(A, B, K)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # A, B = 3, 3
    # for k in range(30):
    #     solve(A, B, k)
