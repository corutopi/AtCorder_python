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
def solve(N, C, abc):
    service_in = []
    service_out = []
    service_cost = []
    p_in = 0
    p_out = 0
    for i in range(N):
        a, b, c = abc[i]
        b += 1
        service_in.append([a, i])
        service_out.append([b, i])
        service_cost.append(c)
    service_in.sort()
    service_in.append([inf, N])
    service_out.sort()
    service_out.append([inf, N])
    service_cost.append(0)

    before_day = 0
    total_cost = 0
    day_cost = 0
    resume_cost = 0
    while p_in < N or p_out < N:
        # tmp_cost = 0
        next_day = min(service_in[p_in][0], service_out[p_out][0])
        while service_in[p_in][0] == next_day:
            day_cost += service_cost[service_in[p_in][1]]
            p_in += 1
        while service_out[p_out][0] == next_day:
            day_cost -= service_cost[service_out[p_out][1]]
            p_out += 1
        total_cost += (next_day - before_day) * resume_cost
        before_day = next_day
        # day_cost += tmp_cost
        resume_cost = min(day_cost, C)
    print(total_cost)


if __name__ == '__main__':
    N, C = map(int, input().split())
    abc = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, C, abc)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
