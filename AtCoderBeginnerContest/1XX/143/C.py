# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, S):
    fusioned = S[0]
    for s in S:
        if fusioned[-1] != s:
            fusioned += s
    print(len(fusioned))


if __name__ == '__main__':
    N = int(input())
    S = input()
    solve(N, S)
