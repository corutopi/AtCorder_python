# import sys
# sys.setrecursionlimit(10 ** 6)
import bisect


# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    ans = N
    A.sort()
    visited = [False] * N
    a_max = A[-1]
    for i in range(N):
        if visited[i]: continue
        tmp = A[i]
        visited[i] = True
        while tmp * 2 <= a_max:
            tmp *= 2
            idx_2a = bisect.bisect_right(A, tmp) - 1
            if tmp == A[idx_2a]:
                ans -= 1
                visited[idx_2a] = True
    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # N = 10 ** 5
    # A = [N - i for i in range(N)]
    # A = [1] + [10 ** 9 - i for i in range(N)]
    # # N = 5
    # # A = [2, 3, 7, 6, 8]
    # print(N)
    # print(A)
    # solve(N, A)
