# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(A):
    if len(A) == 1:
        print(0)
        return

    key_count = 0
    for i in range(len(A) // 2):
        if A[i] != A[-(1 + i)]:
            key_count += 1
    ans = 0
    for i in range(len(A)):
        if len(A) % 2 == 1 and i == len(A) // 2:
            # center char depends on the state of other characters
            if key_count == 0:
                ans += 0
            else:
                ans += 25
        elif A[i] == A[-(1 + i)]:
            ans += 25  # can change anyone
        elif key_count == 1:
            ans += 24  # can change chara diff from the pair
        else:
            ans += 25  # can change anyone (other pairs diff)
    print(ans)


if __name__ == '__main__':
    A = input()
    solve(A)

    # # test
    # from random import randint
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
