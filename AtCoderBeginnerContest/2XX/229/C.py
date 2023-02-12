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
def solve(N, W, AB):
    AB.sort(reverse=True)
    ans = 0
    cheese = 0
    for i in range(N):
        ong = AB[i][1] if cheese + AB[i][1] <= W else W - cheese
        ans += AB[i][0] * ong
        cheese += ong

    print(ans)


if __name__ == '__main__':
    N, W = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, W, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
