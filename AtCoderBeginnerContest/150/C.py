# import sys
# sys.setrecursionlimit(10 ** 6)
import bisect
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, Ps, Qs):
    def dfs(s, perm):
        if len(s) == N + 1:
            perm.append(int(s))
            return perm
        for i in range(1, N + 1):
            if not str(i) in s:
                perm = dfs(s + str(i), perm)
        return perm

    perm = dfs('0', [])

    p = int(''.join(Ps))
    q = int(''.join(Qs))

    print(abs(bisect.bisect_right(perm, p) - bisect.bisect_right(perm, q)))


if __name__ == '__main__':
    N = int(input())
    Ps = input().split()
    Qs = input().split()
    solve(N, Ps, Qs)
