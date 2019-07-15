"""
C - Synthetic Kadomatsu
"""


def solve():
    # データ読込
    N, A, B, C = map(int, input().split())
    bamboos = [int(input()) for n in range(N)]
    MP = 0

    # 小さい竹Xから作っていく
    for i in [C, B, A]:  # 小さい順
        while True:
            abs_num = [abs(i - b) for b in bamboos]
            t = abs_num.index(min(abs_num))
            if min(abs_num) < 10 or bamboos[t] > i:
                MP += abs(i - bamboos[t])
                bamboos.remove(t)
                break
            else:
                add_list = [b for b in bamboos if b < abs_num[t] * 2]
                add_list


    print(MP)


    # ①一番長さの近い竹を見繕う
    # ②竹とXの差が10以内なら延長/短縮魔法を使う
    # ③異なる場合
    # ③-1 竹がXより小さい場合、足して差を10以上値締められる竹がないか探す.
    #      あれば足す
    # ③-2 竹がXより大きい場合、選んだ竹より小さくて竹を合計


    10, 100, 1000
    1
    1
    1


if __name__ == '__main__':
    solve()
