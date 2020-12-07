# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(first, last, N, s):
    tree = {}
    s = list(set([first] + s + [last]))
    [tree.setdefault(ss, []) for ss in s]
    visited = {}
    [visited.setdefault(ss, False) for ss in s]

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            si = s[i]
            sj = s[j]
            cnt = 0
            for k in range(len(si)):
                if si[k] != sj[k]:
                    cnt += 1
                    if cnt > 1:
                        break
            if cnt == 1:
                tree[si].append(sj)
                tree[sj].append(si)

    dq = deque([[first, 0, []]])
    ans = -1
    ans_list = []
    while dq:
        now, cnt, lst = dq.popleft()
        lst.append(now)
        if now == last:
            ans = min(ans, cnt) if ans != -1 else cnt
            ans_list = lst
            break
        visited[now] = True
        for nxt in tree[now]:
            if visited[nxt]:
                continue
            dq.append([nxt, cnt + 1, lst.copy()])
    print(max(ans - 1, 0) if ans != -1 else ans)
    for al in ans_list:
        print(al)
    if len(ans_list) == 1:
        print(ans_list[0])


if __name__ == '__main__':
    first, last = input().split()
    N = int(input())
    s = [input() for _ in range(N)]
    solve(first, last, N, s)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # first, last = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', \
    #               'aaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
    # N = 1000
    # s = []
    # tmp = first
    # for _ in range(N):
    #     i = randint(0, len(first) - 1)
    #     c = random_str(1, 'abcdefghijklmnopqrstuvwxyz')
    #     tmp = tmp[:i] + c + tmp[i + 1:]
    #     s.append(tmp)
    # last = s[-1]
    # solve(first, last, N, s)
