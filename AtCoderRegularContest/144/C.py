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

"""
a <= b -> a <= b + EPS
a < b  -> a < b - EPS
a == b -> abs(a - b) < EPS
"""
EPS = 10 ** -7


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K):
    if K > N // 2:
        print(-1)
        return -1
    n = N
    oneset = K * 2
    ans = []
    for i in range(N // (oneset)):
        tmp = oneset
        n -= oneset
        if 0 < n < oneset:
            tmp += n
            x = []
            if n > K:
                base = i * oneset + 1
                x += [j + K + base for j in range(K)]
                x += [j + base for j in range(n - K)]
                x += [j + base for j in range(tmp - K, tmp)]
                x += [j + base + (n - K) for j in range(K - (n - K))]
                x += [tmp + base - j - K for j in range(n - K, 0, -1)]
            else:
                x += [(j + K) % tmp + i * oneset + 1 for j in range(tmp)]
            ans += x
        else:
            ans += [(j + K) % tmp + i * oneset + 1 for j in range(tmp)]
    print(*ans)
    return ans


def solve_force(N, K):
    if K > N // 2:
        return -1
    import itertools
    arr = [i + 1 for i in range(N)]
    ans = None
    for l in itertools.permutations(arr):
        for i in range(len(l)):
            if abs(l[i] - (i + 1)) < K:
                break
        else:
            if ans is None:
                ans = list(l)
            else:
                ll = list(l)
                ans = ll if ll < ans else ans
    return ans


if __name__ == '__main__':
    N, K = map(int, input().split())
    solve(N, K)
    # print(solve_force(N, K))

    # # test
    # from random import randint
    #
    # # import string
    # # import tool.testcase as tt
    # # from tool.testcase import random_str, random_ints
    # # solve()
    # cnt = 0
    # flg = False
    # for i in range(11, 12):
    #     for j in range(1, i):
    #         a = solve(i, j)
    #         b = solve_force(i, j)
    #         if b != a:
    #             print(i, j)
    #             print(a)
    #             print(b)
    #             flg = True
    #             break
    #     if flg: break
    #     print('complete {}'.format(i))

    # while True:
    #     N = randint(5, 10)
    #     K = randint(1, N // 2)
    #     a = solve(N, K)
    #     b = solve_force(N, K)
    #     if b != a:
    #         print(N, K)
    #         print(a)
    #         print(b)
    #         break
    #     cnt += 1
    #     if cnt % 10 == 0:
    #         print(cnt)
