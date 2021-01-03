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
def solve(N, C, A):
    num_map = [[] for _ in range(C + 1)]
    for i in range(N):
        num_map[A[i]].append(i + 1)
    for i in range(1, C + 1):
        ans = 0
        tgt_map = num_map[i]
        for j in range(len(tgt_map)):
            now = tgt_map[j]
            if j == 0:
                ans += now * (N - now + 1)
            else:
                bfr = tgt_map[j - 1]
                ans += (now - bfr) * (N - now + 1)
        print(ans)


if __name__ == '__main__':
    N, C = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, C, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
