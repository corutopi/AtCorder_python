# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(a, b, x, y):
    ans = 0
    if a == b:
        ans = x
    elif a < b:
        ans = min(x + y * abs(a - b), x * (abs(a - b) * 2 + 1))
    else:
        ans = min(x + y * (abs(a - b) - 1), x * (abs(a - b) * 2 - 1))
    print(ans)


if __name__ == '__main__':
    a, b, x, y = map(int, input().split())
    solve(a, b, x, y)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
