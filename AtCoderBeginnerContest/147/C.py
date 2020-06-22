# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, XYs):
    ans = 0
    for i in range(2 ** N):
        for j in range(N):
            if (i >> j) & 1:
                for x, y in XYs[j + 1]:
                    if ((i >> (x - 1)) & 1) ^ y:
                        break
                else:
                    continue
                break
        else:
            ans = max(ans, bin(i).count('1'))
    print(ans)


if __name__ == '__main__':
    N = int(input())
    XYs = [[] for _ in range(N + 1)]
    for i in range(N):
        Ai = int(input())
        for _ in range(Ai):
            XYs[i + 1].append([int(i) for i in input().split()])
    # N = 15
    # XYs = [[] for _ in range(N + 1)]
    # for i in range(N):
    #     for j in range(15):
    #         if i == j:
    #             continue
    #         XYs[i + 1].append([j + 1, 1])
    # print(N)
    # for i in range(len(XYs)):
    #     print(i, XYs[i])
    solve(N, XYs)
