# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(X, Y, A, B):
    ans = 0
    for i in range(int(10 ** 19)):
        tmp = X * (A ** i)
        if tmp >= Y: break
        ans = max(ans, i + (Y - 1 - tmp) // B)
    print(ans)


if __name__ == '__main__':
    X, Y, A, B = map(int, input().split())
    solve(X, Y, A, B)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
