# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
import collections


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, Vi):
    V1 = Vi[::2]
    V2 = Vi[1::2]
    c_V1 = dict(collections.Counter(V1))
    c_V2 = dict(collections.Counter(V2))
    c_V1 = sorted(c_V1.items(), key=lambda x: x[1], reverse=True)
    c_V2 = sorted(c_V2.items(), key=lambda x: x[1], reverse=True)
    c_V1.append((-1, 0))
    c_V2.append((-1, 0))
    ans = 0
    if c_V1[0][0] == c_V2[0][0]:
        ans = min(len(V1) - c_V1[0][1] + len(V2) - c_V2[1][1],
                  len(V1) - c_V1[1][1] + len(V2) - c_V2[0][1])
    else:
        ans = len(V1) - c_V1[0][1] + len(V2) - c_V2[0][1]
    print(ans)


if __name__ == '__main__':
    N = int(input())
    Vi = [int(i) for i in input().split()]
    solve(N, Vi)

    # # test
    # from random import randint
    # from func import random_str

