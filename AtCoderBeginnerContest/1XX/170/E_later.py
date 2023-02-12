## over 7sec
# import sys
# sys.setrecursionlimit(10 ** 6)
import bisect

# from collections import deque
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, Q, AB, CD):
    AB = [[0, 0]] + AB
    child_code = [AB[i][0] * 10 ** 6 + i for i in range(N + 1)]
    en = [[] for _ in range(2 * 10 ** 5 + 1)]
    for i in range(1, N + 1):
        a, b = AB[i]
        en[b].append(child_code[i])

    rep = []
    for e in en:
        if len(e) == 0:
            continue
        e.sort()
        rep.append(e[-1])
    rep.sort()

    for c, d in CD:
        cc = child_code[c]
        from_en = en[AB[c][1]]
        c_idx = bisect.bisect_left(from_en, cc)
        del from_en[c_idx]
        if len(from_en) == 0:
            del rep[bisect.bisect_left(rep, cc)]
        elif cc > from_en[-1]:
            rep.insert(bisect.bisect_left(rep, from_en[-1]), from_en[-1])
            del rep[bisect.bisect_left(rep, cc)]

        to_en = en[d]
        if len(to_en) == 0:
            to_en.append(cc)
            if len(rep) == 0 or rep[-1] < cc:
                rep.append(cc)
            else:
                rep.insert(bisect.bisect(rep, cc), cc)
        else:
            if to_en[-1] < cc:
                rm_cc = to_en[-1]
                to_en.append(cc)
                del rep[bisect.bisect_left(rep, rm_cc)]
                if rep[-1] < cc:
                    rep.append(cc)
                else:
                    rep.insert(bisect.bisect(rep, cc), cc)
            else:
                to_en.insert(bisect.bisect_left(to_en, cc), cc)
        print(rep[0] // 10 ** 6)
        AB[c][1] = d


if __name__ == '__main__':
    N, Q = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    CD = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, Q, AB, CD)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # N, Q = 2 * 10 ** 5, 2 * 10 ** 5
    # AB = [[randint(1, 10 ** 9), randint(1, 2 * 10 ** 5)] for _ in range(N)]
    # CD = [[randint(1, N), randint(1, 2 * 10 ** 5)] for _ in range(Q)]
    # solve(N, Q, AB, CD)
