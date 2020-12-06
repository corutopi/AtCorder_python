# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, S):
    s = 0
    length = 1
    while True:
        tmp = S[s:s + length]
        if S[s + length:].find(tmp) >= 0:
            length += 1
        else:
            s += 1
        if s + length * 2 > N:
            break
    print(length - 1)


if __name__ == '__main__':
    N = int(input())
    S = input()
    solve(N, S)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # N = 5 * 10 ** 3
    # S = random_str(N, 'a')
    # solve(N, S)
