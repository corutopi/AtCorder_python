# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    dq = deque(A)
    ans = 0
    while len(dq) > 1:
        l1, l2 = dq[0], dq[1]
        r1, r2 = dq[-1], dq[-2]
        if l1 + 1 + l1 + l2 < r1 + 1 + r1 + r2:
            ans += l1 + 1 + l1 + l2
            a, b, c = dq.popleft(), dq.popleft(), dq.popleft()
            dq.appendleft(a + b + c + 2)
        else:
            ans += r1 + 1 + r1 + r2
            a, b, c = dq.pop(), dq.pop(), dq.pop()
            dq.append(a + b + c + 2)
    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
