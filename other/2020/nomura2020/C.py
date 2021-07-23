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
    all_leaf = sum(A)
    node = 1
    for i in range(N + 1):
        ans += node
        if node < A[i]:
            print(-1)
            return
        node -= A[i]
        all_leaf -= A[i]
        node = min(node * 2, all_leaf)
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
