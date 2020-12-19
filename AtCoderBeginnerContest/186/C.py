# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    ans = 0
    for n in range(1, N + 1):
        tmp = n
        flg = True
        while tmp > 0:
            tmp, d = divmod(tmp, 10)
            if d == 7:
                flg = False
                break
        tmp = n
        while tmp > 0:
            tmp, d = divmod(tmp, 8)
            if d == 7:
                flg = False
                break
        if flg:
            ans += 1
    print(ans)


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
