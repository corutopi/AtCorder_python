# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(X):
    digit = len(str(X))
    ans = 1
    while ans < X:
        for i in range(1, 10):
            for j in range(9, -1, -1):
                tmp = ''
                for _ in range(digit):
                    if tmp == '':
                        tmp += str(i)
                        continue
                    n = int(tmp[-1]) - j
                    if n < 0:
                        break
                    tmp += str(n)
                else:
                    ans = int(tmp)
                if ans >= X:
                    break
            if ans >= X:
                break
            for j in range(0, 10):
                tmp = ''
                for _ in range(digit):
                    if tmp == '':
                        tmp += str(i)
                        continue
                    n = int(tmp[-1]) + j
                    if n >= 10:
                        break
                    tmp += str(n)
                else:
                    ans = int(tmp)
                if ans >= X:
                    break
            if ans >= X:
                break
    print(ans)


if __name__ == '__main__':
    X = int(input())
    solve(X)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
