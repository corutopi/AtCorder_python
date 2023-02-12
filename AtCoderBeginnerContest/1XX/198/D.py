# 解説を参考に作成
"""
解くときに見たわけじゃないけど以下は参考になりそう。速い...
    https://atcoder.jp/contests/abc198/submissions/26815451
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
import itertools
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch

S1 = input()
S2 = input()
S3 = input()

# # test
# from random import randint
# import string
# import tool.testcase as tt
# from tool.testcase import random_str, random_ints
# solve()


alp = list(set(S1 + S2 + S3))

if len(alp) > 10:
    print('UNSOLVABLE')
    exit()

for x in itertools.permutations([str(i) for i in range(10)], len(alp)):
    X = S1 + S2 + S3
    for i, y in enumerate(x):
        X = X.replace(alp[i], y)
    a, b, c = X[:len(S1)], X[len(S1): len(S1) + len(S2)], X[len(S1) + len(S2):]

    # a, b, c = S1, S2, S3
    # for i, y in enumerate(x):
    #     a = a.replace(alp[i], y)
    #     b = b.replace(alp[i], y)
    #     c = c.replace(alp[i], y)

    if '0' in (a[0], b[0], c[0]):
        continue
    if int(a) + int(b) == int(c):
        print(a)
        print(b)
        print(c)
        exit()

print('UNSOLVABLE')