# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, D):
    ans = N
    while True:
        flg = True
        for s in str(ans):
            if s in D:
                flg = False
                break
        if flg:
            break
        ans += 1
    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    D = input().split()
    solve(N, K, D)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
