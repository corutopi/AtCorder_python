def solve():
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    A.sort()
    CB = [list(reversed([int(i) for i in input().split()])) for _ in range(M)]
    CB = list(sorted(CB, reverse=True))

    change_list = []  # 値を変更した数の変更後の値を入れる
    no_A_flag = False
    for CiBi in CB:
        for i in range(CiBi[1]):
            if A[0] < CiBi[0]:
                change_list.append(CiBi[0])
                A.pop(0)  # 変更した値は以後変更対象となることはないのでリストから出す
                if len(A) == 0:
                    # 値をすべて変更し終わったた場合はその時点で処理終了
                    no_A_flag = True
                    break
            else:
                if i == 0:
                    # 最初の時点で変更対象外なら以降のループは行う必要がない
                    no_A_flag = True
                break
        if no_A_flag:
            break  # 変更するものがなくなれば出る
        # A.sort()

    print(sum(A) + sum(change_list))


if __name__ == '__main__':
    solve()
