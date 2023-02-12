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
def solve(N, A, B, C, S):
    ans = []
    sum_num = sum([A, B, C])
    num_dict = {'A': A, 'B': B, 'C': C}
    for i in range(N):
        s = S[i]
        if num_dict[s[0]] == num_dict[s[1]] == 0:
            print('No')
            return
        if sum_num == 2 and num_dict[s[0]] == num_dict[s[1]] == 1:
            if i < N - 1 and s[0] in S[i + 1]:
                ans.append(s[0])
                num_dict[s[0]] += 1
                num_dict[s[1]] -= 1
            else:
                ans.append(s[1])
                num_dict[s[1]] += 1
                num_dict[s[0]] -= 1
        else:
            if num_dict[s[0]] >= num_dict[s[1]]:
                h = s[0]
                l = s[1]
            else:
                h = s[1]
                l = s[0]
            ans.append(l)
            num_dict[l] += 1
            num_dict[h] -= 1
    print('Yes')
    [print(a) for a in ans]


if __name__ == '__main__':
    N, A, B, C = map(int, input().split())
    S = [input() for _ in range(N)]
    solve(N, A, B, C, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
