# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, Bs):
    Bss = [Bs[0]] + Bs + [Bs[-1]]
    As = []
    for i in range(len(Bss) - 1):
        As.append(min(Bss[i], Bss[i + 1]))
    print(sum(As))


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    # As = [int(i) for i in input().split()]
    Bs = [int(i) for i in input().split()]
    solve(N, Bs)
