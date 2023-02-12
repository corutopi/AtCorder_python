# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    A1_sum = [0]
    A2_sum = [0]
    for i in range(N):
        A1_sum.append(A1_sum[-1] + A[0][i])
        A2_sum.append(A2_sum[-1] + A[1][i])
    ans = 0
    for i in range(1, N + 1):
        ans = max(ans, A1_sum[i] + (A2_sum[-1] - A2_sum[i - 1]))
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    A = [[int(i) for i in input().split()] for _ in range(2)]
    solve(N, A)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
