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
    circle = [0] * (N + 1)
    print(0)
    tmp = mail_code(input())
    if tmp == 0:
        return
    circle[0] = tmp
    circle[-1] = tmp
    l, r = 0, N
    for _ in range(20):
        m = (l + r) // 2
        print(m)
        tmp = mail_code(input())
        if tmp == 0:
            return
        circle[m] = tmp
        if (circle[l] == tmp and (m - l) % 2 == 1) or \
                (circle[l] != tmp and (m - l) % 2 == 0):
            r = m
        else:
            l = m


def mail_code(s):
    return 1 if s == 'Male' else 2 if s == 'Female' else 0


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
