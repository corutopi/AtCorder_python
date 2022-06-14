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


def cmb(n, r):
    """組み合わせ"""
    import math
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A, B, V):
    V.sort(reverse=True)
    max_avg = sum(V[:A]) / A
    key = V[A - 1]
    pattern = 0
    # 最大値のみを使用する場合
    if key == V[0]:
        key_num = sum(1 if v == key else 0 for v in V)
        for i in range(A, min(B, key_num) + 1):
            pattern += cmb(key_num, i)
    # A番目の値が複数ある場合
    elif key in (V[A - 2], V[A]):
        key_num = sum(1 if v == key else 0 for v in V)
        key_start = 0
        for i in range(N):
            if V[i] == key:
                key_start = i
                break
        pattern = cmb(key_num, A - key_start)
    # それ以外
    else:
        pattern = 1

    print(max_avg)
    print(pattern)


if __name__ == '__main__':
    N, A, B = map(int, input().split())
    V = [int(i) for i in input().split()]
    solve(N, A, B, V)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
