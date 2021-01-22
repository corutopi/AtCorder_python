# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, C, stc):
    channel = [[] for _ in range(C + 1)]
    for s, t, c in stc:
        channel[c].append([s, t])
    for i in range(len(channel)):
        cnl = channel[i]
        cnl.sort()
        tmp = []
        m = 0
        for j in range(len(cnl)):
            if j < len(cnl) - 1 and cnl[j][1] == cnl[j + 1][0]:
                if m == 0:
                    m = cnl[j][0]
                continue
            if m != 0:
                tmp.append([m, cnl[j][1]])
                m = 0
            else:
                tmp.append([cnl[j][0], cnl[j][1]])
        channel[i] = tmp

    tv_end = max([t for s, t, c in stc]) * 10
    time = [[0, 0] for _ in range(tv_end + 1)]
    for cnl in channel:
        for s, t in cnl:
            time[s * 10 - 5][0] += 1
            time[t * 10][1] += 1
    # for s, t, c in stc:
    #     time[s * 10 - 5][0] += 1
    #     time[t * 10][1] += 1
    ans = 0
    tv_num = 0
    for j in range(tv_end + 1):
        tv_num += time[j][0]
        tv_num -= time[j][1]
        ans = max(ans, tv_num)
    print(ans)


if __name__ == '__main__':
    N, C = map(int, input().split())
    stc = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, C, stc)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
