# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    s = [0] * N
    alp = 'abcdefghij'

    def up(s, rank):
        if rank == len(s):
            s[- rank] += 1
        else:
            m = max(s[:- rank])
            if m >= s[- rank]:
                s[- rank] += 1
            else:
                s[- rank] = 0
                s = up(s, rank + 1)
        return s

    while s[0] == 0:
        print(''.join([alp[ss] for ss in s]))
        s = up(s, 1)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
