# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, X, S):
    ans = X
    for s in S:
        if s == 'x':
            ans = max(0, ans - 1)
        else:
            ans += 1
    print(ans)


if __name__ == '__main__':
    N, X = map(int, input().split())
    S = input()
    solve(N, X, S)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
