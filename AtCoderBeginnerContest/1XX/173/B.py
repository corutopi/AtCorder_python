# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, Ss):
    cntAC, cntWA, cntTLE, cntRE = 0, 0, 0, 0
    cntJudge = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
    for S in Ss:
        cntJudge[S] += 1
    print('AC x ' + str(cntJudge['AC']))
    print('WA x ' + str(cntJudge['WA']))
    print('TLE x ' + str(cntJudge['TLE']))
    print('RE x ' + str(cntJudge['RE']))


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    # As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    Ss = [input() for _ in range(N)]
    solve(N, Ss)
