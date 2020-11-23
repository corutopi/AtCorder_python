# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(A, B):
    # search diff char, same char num
    same_char = {}
    diff_num = 0
    A_diffs = ''
    B_diffs = ''
    for i in range(len(A)):
        a = A[i]
        b = B[i]
        same_char.setdefault(a, 0)
        same_char[a] += 1
        if a != b:
            diff_num += 1
            A_diffs += a
            B_diffs += b
    A_diffs_sort = ''.join(sorted(A_diffs))
    B_diffs_sort = ''.join(sorted(B_diffs))

    def swap_cmb_count(x, y):
        visited = [False] * len(x)
        re = 0
        for i in range(len(x)):
            xx = x[i]
            yy = y[i]
            for j in range(i + 1, len(x)):
                if visited[j]: continue
                if x[j] == yy and y[j] == xx:
                    re += 1
                    visited[j] = True
        return re

    swap_cnt = swap_cmb_count(A_diffs, B_diffs)
    same_char_num = max(same_char.values())
    ans = 'NO'
    # 1. more than 7 -> NO
    if diff_num >= 7:
        pass
    # 2. not same cmb -> NO
    elif A_diffs_sort != B_diffs_sort:
        pass
    # 3. pattern 6: all(3) swap cmb
    elif diff_num == 6:
        if swap_cnt == 3:
            ans = 'YES'
    # 4. pattern 5: one swap cmb
    elif diff_num == 5:
        if swap_cnt == 1:
            ans = 'YES'
    # 5. pattern 4: no swap cmb or all(2) swap cmb and exist same char
    elif diff_num == 4:
        if swap_cnt == 0:
            ans = 'YES'
        if swap_cnt == 2 and same_char_num >= 2:
            ans = 'YES'
    # 6. pattern 3: exist same char
    elif diff_num == 3:
        if same_char_num >= 2:
            ans = 'YES'
    # 7. pattern 2: all clear
    elif diff_num == 2:
        ans = 'YES'
    # 8. pattern 1: nothing (same of 'not same cmb')
    elif diff_num == 1:
        pass
    # 9. pattern 0: exist same char
    elif diff_num == 0:
        if same_char_num >= 2:
            ans = 'YES'
    print(ans)


if __name__ == '__main__':
    A, B = input(), input()
    solve(A, B)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve('abababab', 'babababa')  # 7
    # solve('aaaaaaaa', 'aaaaaaab')  # not same cmb
    # solve('aaabbbaa', 'bbbaaaaa')  # 6 three swap
    # solve('ababcdaa', 'babcdaaa')  # 6 one swap
    # solve('abcdeaaa', 'badecaaa')  # 5 one swap
    # solve('abcdeaaa', 'bcdeaaaa')  # 5 no swap
    # solve('abcdaaaa', 'bcdaaaaa')  # 4 no swap
    # solve('abcdefgh', 'badcefgh')  # 4 two swap and no same
    # solve('abcdefga', 'badcefga')  # 4 two swap and two same
    # solve('abcdefgh', 'bcadefgh')  # 3 no same
    # solve('abcdefga', 'bcadefga')  # 3 two same
    # solve('abcdefgh', 'bacdefgh')  # 2
    # solve('abcdefgh', 'abcdefgh')  # 0 no same
    # solve('abbcdefg', 'abbcdefg')  # 0 two same
