# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# import string
from heapq import heappush, heappop
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(a, N):
    border = 10 ** 6
    min_list = [-1] * (border + 1)
    min_list[1] = 0
    visited_list = [0] * (border + 1)
    dq = deque([1])
    visited_list[1] = 1
    while dq:
        now = dq.popleft()
        t1 = now * a
        if t1 < border and visited_list[t1] != 1:
            visited_list[t1] = 1
            min_list[t1] = min_list[now] + 1
            dq.append(t1)
            # if t1 == 767090:
            #     t1 = t1
        t2 = now
        cnt = 0
        while t2 >= 10 and t2 % 10 > 0:
            s = str(t2)
            t2 = int(s[-1] + s[:-1])
            cnt += 1
            if t2 < border and visited_list[t2] != 1:
                visited_list[t2] = 1
                min_list[t2] = min_list[now] + cnt
                dq.append(t2)
            # if t2 == 767090:
            #     t2 = t2
            if t2 == now:
                break
    print(min_list[N])


if __name__ == '__main__':
    a, N = map(int, input().split())
    solve(a, N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
