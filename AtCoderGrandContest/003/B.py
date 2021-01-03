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
def solve(N, A):
    ans = 0
    for i in range(N):
        ans += A[i] // 2
        if A[i] % 2 == 1 and i < N - 1 and A[i] > 0:
            ans += 1
            A[i + 1] -= 1
    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
