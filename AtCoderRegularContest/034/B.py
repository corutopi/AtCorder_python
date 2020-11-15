# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    def f(n):
        s = str(n)
        re = 0
        for ss in s:
            re += int(ss)
        return re
    ans = 0
    ans_list = []
    start = max(0, N - 1000)
    for i in range(start, N + 1):
        if N == i + f(i):
            ans += 1
            ans_list.append(i)
    print(ans)
    [print(i) for i in ans_list]


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
