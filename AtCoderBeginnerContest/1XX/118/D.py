"""
Match Matching
"""
def fff(usable):

    pass


def solve():
    number_use_match = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    match_num, number_num = [int(i) for i in input().split()]
    enable_number = [int(i) for i in input().split()]
    usable_number = dict()
    enable_number_match = [number_use_match[i - 1] for i in enable_number]
    print(enable_number)
    print(enable_number_match)
    # マッチの本数を一意にする
    for i, n in enumerate(enable_number_match):
        if enable_number_match.count(n) > 1:
            tag = [x for y, x in enumerate(enable_number) if enable_number_match[y] == n]

    # ①最小のマッチかつ最大の数値で作れるだけ作る
    # ②①で作れるだけ作った数-1だけを実際に作る
    # ③残ったマッチで作れる最大の数値を作る
    # ④マッチが余っていないか確かめる


if __name__ == '__main__':
    solve()
