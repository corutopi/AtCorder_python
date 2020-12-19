# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    A.sort()
    A_sum = [0]
    for a in A:
        A_sum.append(A_sum[-1] + a)
    ans = 0
    for i in range(N - 1):
        ans += (A_sum[-1] - A_sum[i + 1]) - (A[i] * (N - 1 - i))
    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 2 * 10 ** 5
    # A = [randint(1, 10 ** 8) for _ in range(N)]
    # solve(N, A)
