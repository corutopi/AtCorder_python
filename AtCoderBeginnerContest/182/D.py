# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    cumsum_A = [A[0]]
    for i in range(1, N):
        cumsum_A.append(cumsum_A[-1] + A[i])
    ccumsum_A = [0]
    for i in range(N):
        ccumsum_A.append(ccumsum_A[-1] + cumsum_A[i])
    c_max_A = [cumsum_A[0]]
    for i in range(1, N):
        c_max_A.append(max(c_max_A[-1], cumsum_A[i]))
    ans = - (10 ** 18)
    for i in range(N):
        ans = max(ans, ccumsum_A[i], ccumsum_A[i] + c_max_A[i])
    ans = max(ans, ccumsum_A[-1])  # 不要かも
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
