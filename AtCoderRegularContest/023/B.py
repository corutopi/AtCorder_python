# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(R, C, D, A):
    ans = 0
    for r in range(R):
        for c in range(C):
            if r + c <= D and (r + c) % 2 == D % 2:
                ans = max(ans, A[r][c])
    print(ans)


if __name__ == '__main__':
    R, C, D = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(R)]
    solve(R, C, D, A)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
