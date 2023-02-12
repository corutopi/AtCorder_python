# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

"""
a <= b -> a <= b + EPS
a < b  -> a < b - EPS
a == b -> abs(a - b) < EPS
"""
EPS = 10 ** -7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(Q, query):
    note = dict()
    tree = [[0, 0]] + [[] for _ in range(Q)]
    start, end = 0, 0
    ans = []
    for i in range(Q):
        now = i + 1
        action = query[i][0]
        if action == 'ADD':
            tree[now] = [end, query[i][1]]
            end = now
        elif action == 'DELETE':
            if start != end:
                end = tree[end][0]
        elif action == 'SAVE':
            note[query[i][1]] = [start, end]
        elif action == 'LOAD':
            start, end = note.get(query[i][1], [now, now])
        ans.append(-1 if start == end else tree[end][1])
    print(*ans)


if __name__ == '__main__':
    Q = int(input())
    query = [[s for s in input().split()] for _ in range(Q)]
    solve(Q, query)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
