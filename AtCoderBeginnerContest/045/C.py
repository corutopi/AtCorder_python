# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(S):
    N = int(S)
    ans = 0
    for i in range(2 ** (len(S) - 1)):
        before = 0
        for j in range(len(S) - 1):
            if i >> j & 1:
                ans += int(S[before:j + 1])
                before = j + 1
        ans += int(S[before:])
    print(ans)


if __name__ == '__main__':
    S = input()
    solve(S)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
