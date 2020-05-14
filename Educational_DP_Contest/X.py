"""
X - Tower

以下を参考に作成.
https://www.hamayanhamayan.com/entry/2019/01/12/154729

積み重なったブロックの総重量ごとに、その重量で作成できる最大の価値を求めていく.
ブロックは事前にソートする.
"""


class Block:
    def __init__(self, w, s, v):
        self.w = w
        self.s = s
        self.v = v

    def __lt__(self, other):
        return min(self.s, other.s - self.w) > min(other.s, self.s - other.w)

    def __repr__(self):
        return '[w:{} s:{} v:{}]'.format(self.w, self.s, self.v)


def solve():
    N = int(input())
    blocks = []
    for _ in range(N):
        l = [int(i) for i in input().split()]
        blocks.append(Block(l[0], l[1], l[2]))
    print(blocks)
    blocks.sort()
    sorted(blocks)
    print(blocks)
    dp = [] * (10 ** 4 * 2 + 1)


if __name__ == '__main__':
    solve()
