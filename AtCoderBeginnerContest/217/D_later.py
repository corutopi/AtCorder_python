# 解説と以下を参考に作成
# https://kazuma8128.hatenablog.com/entry/2018/05/06/022654
# BinaryTrieの考え方自体はあってるっぽいがTLEになる

# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


class BinaryTrie:
    def __init__(self, b):
        self.bit_size = b
        self.b_node = BinaryNode()

    def insert(self, x):
        self.b_node.add_node(x, self.bit_size)

    def delete(self, x):
        self.b_node.del_node(x, self.bit_size)

    def max_element(self):
        pass

    def min_element(self):
        pass

    def lower_bound(self, x):
        return self.b_node.lower_bound(x, self.bit_size)

    def upper_bound(self, x):
        return self.b_node.num - self.b_node.upper_bound(x, self.bit_size) + 1

    def kth_element(self, k):
        return self.b_node.kth_element(k, self.bit_size)


class BinaryNode:
    def __init__(self):
        self.num = 0
        self.pointer = [None, None]

    def __add_pointer(self, x):
        self.pointer[x] = \
            BinaryNode() if self.pointer[x] is None else self.pointer[x]

    def __del_pointer(self, x):
        self.pointer[x] = None

    def add_node(self, x, b):
        if b == -1:
            self.num += 1
            return self.num
        t = x >> b & 1
        self.__add_pointer(t)
        self.pointer[t].add_node(x, b - 1)
        self.num += 1

    def del_node(self, x, b):
        if b == -1:
            self.num = 0
            return self.num
        t = x >> b & 1
        if self.pointer[t].del_node(x, b - 1) == 0:
            self.__del_pointer(t)
        self.num -= 1
        return self.num

    def upper_bound(self, x, b):
        if b == -1:
            return 1
        re = 0
        if x >> b & 1 == 1:
            if self.pointer[1] is not None:
                re += self.pointer[1].upper_bound(x, b - 1)
        else:
            if self.pointer[0] is not None:
                re += self.pointer[0].upper_bound(x, b - 1)
            if self.pointer[1] is not None:
                re += self.pointer[1].num
        return re

    def lower_bound(self, x, b):
        if b == -1:
            return 1
        re = 0
        if x >> b & 1 == 1:
            if self.pointer[0] is not None:
                re += self.pointer[0].num
            if self.pointer[1] is not None:
                re += self.pointer[1].lower_bound(x, b - 1)
        else:
            if self.pointer[0] is not None:
                re += self.pointer[0].lower_bound(x, b - 1)
        return re

    def kth_element(self, k, b):
        if b == -1:
            return 0
        re = 0
        if self.pointer[0] is not None:
            if k <= self.pointer[0].num:
                re += self.pointer[0].kth_element(k, b - 1)
            else:
                re += 1 << b
                re += self.pointer[1].kth_element(k - self.pointer[0].num,
                                                  b - 1)
        else:
            re += 1 << b
            re += self.pointer[1].kth_element(k, b - 1)
        return re


# from decorator import stop_watch
#
#
# @stop_watch
def solve(L, Q, cx):
    import math
    bt = BinaryTrie(math.ceil(math.log2(L)))
    bt.insert(0)
    bt.insert(L)
    for c, x in cx:
        if c == 1:
            bt.insert(x)
        else:
            a = bt.upper_bound(x)
            print(bt.kth_element(a) -
                  bt.kth_element(a - 1))


if __name__ == '__main__':
    L, Q = map(int, input().split())
    cx = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(L, Q, cx)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # L, Q = 10, 10
    # while True:
    #     cx = [[randint(1, 2), randint(1, L - 1)] for _ in range(Q)]
    #     solve(L, Q, cx)
