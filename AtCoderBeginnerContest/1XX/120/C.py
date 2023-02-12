"""
C - Unification

どんな状況でも赤青両方のブロックが1つ以上存在しているなら赤青となりあう箇所が最低1か所存在する.
→ 赤青どちらかのブロックがなくなるまでブロックを2つずつ取り除くことができる.
"""


def solve():
    S = input()
    zero_num = S.count('0')
    one_num = S.count('1')
    ans = zero_num * 2 if zero_num < one_num else one_num * 2
    print(ans)


if __name__ == '__main__':
    solve()
