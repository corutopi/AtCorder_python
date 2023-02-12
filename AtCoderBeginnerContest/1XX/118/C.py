"""
Monsters Battle Royale
"""


def solve():
    pass
    '''データインプット'''
    monster_num = int(input())
    monster_hp = [int(i) for i in input().split()]
    '''れっつろわいある'''
    while True:
        # 最小の数値minを求める.
        minmum = min(monster_hp)
        # minで他の数値を割り、余りを求める.
        monster_hp = [i % minmum for i in monster_hp]
        monster_hp = [i for i in monster_hp if i != 0]
        #   ここで、余りが0ならば解はminとなる
        if sum(monster_hp) == 0:
            break
        else:
            monster_hp.append(minmum)
    print(minmum)


if __name__ == '__main__':
    solve()
