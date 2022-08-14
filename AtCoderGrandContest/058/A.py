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
def solve(N, P):
    PP = P.copy()
    ans = []
    # for i in range(N * 2 - 1):
    #     if i % 2 == 0:
    #         if PP[i] > PP[i + 1]:
    #             ans.append(i + 1)
    #             PP[i], PP[i + 1] = PP[i + 1], PP[i]
    #     else:
    #         if PP[i] < PP[i + 1]:
    #             ans.append(i + 1)
    #             PP[i], PP[i + 1] = PP[i + 1], PP[i]
    # if len(ans) > N:
    #     PP = P.copy()
    #     ans = []
    #     for i in range(N * 2 - 2, -1, -1):
    #         if i % 2 == 0:
    #             if PP[i] > PP[i + 1]:
    #                 ans.append(i + 1)
    #                 PP[i], PP[i + 1] = PP[i + 1], PP[i]
    #         else:
    #             if PP[i] < PP[i + 1]:
    #                 ans.append(i + 1)
    #                 PP[i], PP[i + 1] = PP[i + 1], PP[i]
    for i in range(N * 2 - 1):
        if i % 2 == 0:
            if PP[i] > PP[i + 1]:
                if i < N * 2 - 2 and PP[i] < P[i + 2]:
                    ans.append(i + 1 + 1)
                    PP[i + 1], PP[i + 2] = PP[i + 2], PP[i + 1]
                else:
                    ans.append(i + 1)
                    PP[i], PP[i + 1] = PP[i + 1], PP[i]
        else:
            if PP[i] < PP[i + 1]:
                if i < N * 2 - 2 and PP[i] > P[i + 2]:
                    ans.append(i + 1 + 1)
                    PP[i + 1], PP[i + 2] = PP[i + 2], PP[i + 1]
                else:
                    ans.append(i + 1)
                    PP[i], PP[i + 1] = PP[i + 1], PP[i]
    print(len(ans))
    if len(ans) != 0:
        print(*ans)
    return ans


if __name__ == '__main__':
    N = int(input())
    P = [int(i) for i in input().split()]
    solve(N, P)

    # N = 3
    # P = [4, 2, 5, 1, 6, 3]
    # solve(N, P)

    # # test
    # from random import randint, shuffle
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # while True:
    #     N = randint(5, 10)
    #     P = [i + 1 for i in range(N * 2)]
    #     shuffle(P)
    #     PP = P.copy()
    #     a = solve(N, P)
    #     if len(a) > N:
    #         print(N)
    #         print(PP)
    #         print(a)
    #         break
