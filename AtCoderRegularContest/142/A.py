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
def solve(N, K):
    r_K = int(str(K)[::-1])
    ans = 0
    if r_K < K:
        ans = 0
    # N < K or N < revers(K)
    elif N < min(K, r_K):
        ans = 0
    # 末尾に0
    elif K != int(str(r_K)[::-1]):
        ans = 1 if K <= N else 0
    # 反転しても同じ数字
    elif K == r_K:
        ans = 0
        tmp = K
        while tmp <= N:
            ans += 1
            tmp *= 10
    # other
    else:
        ans = 0
        tmp = K
        while tmp <= N:
            ans += 1
            tmp *= 10
        tmp = r_K
        while tmp <= N:
            ans += 1
            tmp *= 10
    print(ans)
    # return ans


def int_revers(x):
    return int(str(x)[::-1])


def solve_force(N, K):
    ans = 0
    for i in range(1, N + 1):
        if i == K:
            ans += 1
            continue
        x = int_revers(i)
        if x == K:
            ans += 1
            continue
        x = int_revers(x)
        if x == K:
            ans += 1
    # print(ans)
    return ans


if __name__ == '__main__':
    N, K = map(int, input().split())
    solve(N, K)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # # solve()
    # while True:
    #     N, K = random_ints(2, 1, 1000)
    #     x, y = solve(N, K), solve_force(N, K)
    #     if x != y:
    #         print(N, K)
    #         print(x, y)
    #         break
