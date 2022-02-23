# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor
import re


# inf = float('inf')
# mod = 10 ** 9 + 7
# mod2 = 998244353


def is_word(s):
    if s == '': return False
    for i, c in enumerate(s):
        if i == 0:
            if not re.search('[a-z]', c):
                return False
        else:
            if not re.search('[a-z,0-9]', c):
                return False
    return True


def is_camel(s):
    s = s.strip('_')
    words = []
    t = 0
    for i in range(len(s)):
        if re.search('[A-Z]', s[i]) and i != 0:
            words.append(s[t:i])
            t = i
    else:
        words.append(s[t:])
    for i, w in enumerate(words):
        if i != 0:
            w = w.lower()
        if not is_word(w):
            return False
    return True


def is_snake(s):
    s = s.strip('_')
    words = s.split('_')
    for w in words:
        if not is_word(w):
            return False
    return True


def convert_camel_to_snake(s):
    head_ = 0
    for i in range(len(s)):
        if s[i] == '_': continue
        head_ = i
        break
    tail_ = 0
    for i in range(len(s)):
        if s[len(s) - i - 1] == '_': continue
        tail_ = i
        break
    s = s.strip('_')

    words = []
    t = 0
    for i in range(len(s)):
        if re.search('[A-Z]', s[i]) and i != 0:
            words.append(s[t:i])
            t = i
    else:
        words.append(s[t:])

    return '_' * head_ + '_'.join([w.lower() for w in words]) + '_' * tail_


def convert_snake_to_camel(s):
    head_ = 0
    for i in range(len(s)):
        if s[i] == '_': continue
        head_ = i
        break
    tail_ = 0
    for i in range(len(s)):
        if s[len(s) - i - 1] == '_': continue
        tail_ = i
        break
    s = s.strip('_')
    words = s.split('_')

    return '_' * head_ + \
           ''.join([words[0]] + [w[0].upper() + w[1:] for w in words[1:]]) + \
           '_' * tail_


# from decorator import stop_watch
#
#
# @stop_watch
def solve(S):
    ans = S
    if len(ans.strip('_')) == 0:
        pass
    elif is_camel(S):
        ans = convert_camel_to_snake(S)
    elif is_snake(S):
        ans = convert_snake_to_camel(S)
    print(ans)
    # return ans


if __name__ == '__main__':
    S = input()
    solve(S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve('_d_b_ba')
    #
    # try:
    #     s = ''
    #     while True:
    #         s = random_str(randint(1, 15), '___abcdAB1')
    #         solve(s)
    # finally:
    #     print(s)
    #     pass
    # while True:
    #     s = random_str(randint(1, 5), '___abcdAB1')
    #     if s != solve(solve(s)):
    #         print(s)
    #         print(solve(s))
    #         print(solve(solve(s)))
    #         break
