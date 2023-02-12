# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, A):
    from math import ceil
    A.sort()
    whites = []
    now = 0
    for a in A:
        if a == now + 1:
            pass
        else:
            whites.append(a - now - 1)
        now = a
    if now < N:
        whites.append(N - now)
    if len(whites) == 0:
        print(0)
        return
    k = min(whites)
    ans = 0
    for w in whites:
        ans += ceil(w / k)
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, M, A)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
