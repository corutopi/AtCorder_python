# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
from decorator import stop_watch


@stop_watch
def solve(N, M, ABs):
    ans = 0
    schedule = [0] * M
    max_start_day = [M - i for i in range(M + 1)]
    ABs.sort(key=lambda x: x[1], reverse=True)
    for A, B in ABs:
        if A > M:
            continue
        work_day = max_start_day[A]
        if work_day < 0:
            continue
        flg = False
        while schedule[work_day] != 0:
            work_day -= 1
            if work_day < 0:
                flg = True
                break
        if flg:
            max_start_day[A] = work_day
            continue
        ans += B
        schedule[work_day] = B
        max_start_day[A] = work_day - 1
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    ABs = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, M, ABs)

    # for _ in range(100):
    #     from random import randint
    #     N, M = 10 ** 5, 10 ** 5
    #     ABs = [[randint(1, 10 ** 5), randint(1, 10 ** 4)] for _ in range(10 ** 5)]
    #     solve(N, M, ABs)