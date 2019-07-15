def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    AB_count = 0
    # 元から含まれているABの計算
    head_B_count = 0
    tail_A_count = 0
    B_and_A_count = 0
    for si in S:
        # print(si.count('AB'))
        AB_count += si.count('AB')
        # print(list(si)[0], list(si)[-1])
        list_si = list(si)
        if list_si[0] == 'B' and list_si[-1] == 'A':
            B_and_A_count += 1
            pass
        elif list_si[0] == 'B':
            head_B_count += 1
        elif list_si[-1] == 'A':
            tail_A_count += 1
    if B_and_A_count > 0:
        AB_count += B_and_A_count - 1
        if head_B_count > 0:
            AB_count += 1
            head_B_count -= 1
        if tail_A_count > 0:
            AB_count += 1
            tail_A_count -= 1
    AB_count += min(head_B_count, tail_A_count)
    print(AB_count)


if __name__ == '__main__':
    solve()
