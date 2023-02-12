# import sys
# sys.setrecursionlimit(10 ** 6)
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, pSs):
    result = [0] * (N + 1)
    penalty = [0] * (N + 1)
    for p, S in pSs:
        if S == 'AC':
            result[p] = 1
        else:
            if result[p] == 0:
                penalty[p] += 1
    print(sum(result), sum([result[i] * penalty[i] for i in range(N + 1)]))


if __name__ == '__main__':
    N, M = map(int, input().split())
    pSs = []
    for _ in range(M):
        x = input().split()
        x[0] = int(x[0])
        pSs.append(x)
    solve(N, M, pSs)
