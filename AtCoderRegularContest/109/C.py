# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(n, k, s):
    def judge(x, y):
        if x == y:
            return True
        if (x == 'R' and y == 'S') or \
                (x == 'S' and y == 'P') or \
                (x == 'P' and y == 'R'):
            return True
        return False

    for _ in range(k):
        new_s = ''
        if len(s) % 2 == 1:
            s = s + s
        for i in range(len(s) // 2):
            if judge(s[i * 2], s[i * 2 + 1]):
                new_s += s[i * 2]
            else:
                new_s += s[i * 2 + 1]
        s = new_s
    print(s[0])


if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    solve(n, k, s)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
