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
def solve(N, A):
    b_num = [0] * 30
    for a in A:
        t_a = a
        for i in range(30):
            b_num[i] += t_a & 1
            t_a >>= 1

    exp_2 = [1]
    for _ in range(30):
        exp_2.append(exp_2[-1] * 2)

    ans = 0
    for a in [0] + A:
        t_ans = 0
        t_a = a
        for i in range(30):
            t = b_num[i]
            t = N - b_num[i] if t_a & 1 else t
            t_ans += t * exp_2[i]
            t_a >>= 1
        ans = max(ans, t_ans)

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
    #
    # N = 3 * 10 ** 5
    # A = random_ints(N, 0, 2 ** 30)
    # solve(N, A)
