"""
D - XOR World

解説を参考に作成.
いろいろ試している最中に法則に気付けるチャンスはあった...無念
"""


def solve():
    A, B = map(int, input().split())
    print(all_xor(A - 1) ^ all_xor(B))


def all_xor(num):
    """
    0 ~ numまでのすべての数値の排他的論理和を求める.

    :param num:
    :return:
    """
    if num % 2 == 0:
        if num % 4 == 0:
            return num
        else:
            print('ここ')
            return 1 ^ num
    else:
        if (num + 1) % 4 == 0:
            return 0
        else:
            return 1


def all_xor3(num):
    ans = 0
    for n in range(num + 1):
        ans ^= n
    return ans


def all_xor2(num):
    """
    0 ~ numまでのすべての数値の排他的論理和を求める.

    :param num:
    :return:
    """
    import math
    ans = ''
    num += 1  # 0 を含む
    for n in range(int(math.log2(num)) + 1):
        # 各桁の1の数が奇数ならば1, 異なれば0
        div, mod = divmod(num, 2 ** (n + 1))
        if n == 0 and div % 2 == 1:
            divbin = 1
        else:
            divbin = 0
        if mod <= 2 ** (n + 1):
            modbin = 0
        else:
            if (mod - (2 ** n)) % 2 == 0:
                modbin = 0
            else:
                modbin = 1
        print(n, div, mod, divbin, modbin)
        ans = str(divbin ^ modbin) + ans

        # # 各桁で、ペアにできる01の数と、余る数を数える.
        # div, mod = divmod(num, 2 ** (n + 1))
        # div = div * (2 ** n)  # 二個一の数にする.
        # # divの部分の計算
        # if div % 2 == 0:
        #     divbin = 0
        # else:
        #     divbin = 1
        # # modの部分の計算
        # if mod <= 2 ** (n + 1) / 2:
        #     modbin = 0
        # else:
        #     if (mod - (2 ** (n + 1) / 2)) % 2 == 0:
        #         modbin = 0
        #     else:
        #         modbin = 1
        # print(n, div, mod, divbin, modbin)
        # ans = str(divbin ^ modbin) + ans
    return int(ans, 2)


if __name__ == '__main__':
    # solve()
    n = 1024
    print(bin(n))
    print(all_xor(n))
    print(all_xor2(n))
    print(all_xor3(n))
