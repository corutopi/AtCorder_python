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
def solve(N, A, X):
    sumA = sum(A)
    ans = X // sumA * N
    x = sumA * (X // sumA)
    for i in range(N):
        x += A[i]
        if x > X:
            ans += i + 1
            break
    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    X = int(input())
    solve(N, A, X)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 4
    # A = [1,2,3,4]
    # solve(N, A, 6)
    #
    # for i in range(20):
    #     print("---{}---".format(i))
    #     solve(N, A, i)
