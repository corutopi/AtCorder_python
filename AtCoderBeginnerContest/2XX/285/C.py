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
def solve(S):
    import string
    R = list(reversed(S))
    ans = 0
    for i in range(len(R)):
        if R[i] == 'A':
            ans += 26 ** i
        else:
            ans += 26 ** i * (string.ascii_uppercase.find(R[i]) + 1)
    print(ans)


if __name__ == '__main__':
    S = input()
    solve(S)

    # import string
    # for i in range(1, 100000):
    #     tmp = ''
    #     now = i
    #     for x in range(5, -1, -1):
    #         if now > 26 ** x:
    #             d, now = divmod(now, 26 ** x)
    #             tmp += string.ascii_uppercase.find(d - 1)
    #
    #     pass
