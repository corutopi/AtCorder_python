# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(S):
    ans = 0
    for s in S.split('+'):
        if s.count('*') > 0:
            if not (0 in [int(i) for i in s.split('*')]):
                ans += 1
        else:
            if int(s) != 0:
                ans += 1
    print(ans)


if __name__ == '__main__':
    S = input()
    solve(S)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
