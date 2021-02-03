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
    ans = 0
    A.append(A[-1])
    counter = [0] * (max(A) + 1)
    l = 0
    r = 0
    r_flg = True
    while l < N:
        if r_flg:
            counter[A[r]] += 1
            if counter[A[r]] == 1:
                r += 1
            else:
                r_flg = False
                ans = max(ans, r - l)
        else:
            counter[A[l]] -= 1
            if counter[A[l]] == 1:
                r_flg = True
                r += 1
            l += 1
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
    # solve()
