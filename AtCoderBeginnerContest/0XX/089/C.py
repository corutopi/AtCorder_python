# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, S):
    name_map = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
    key_list = list(name_map.keys())
    for s in S:
        if s[0] in key_list:
            name_map[s[0]] += 1
    num_list = list(name_map.values())
    ans = 0
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            for k in range(j + 1, len(num_list)):
                ans += num_list[i] * num_list[j] * num_list[k]
    print(ans)


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]
    solve(N, S)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
