def solve():
    S = input()
    head2 = int(S[:2])
    tail2 = int(S[2:])
    head_is_mm = False
    if 1 <= head2 <= 12:
        head_is_mm = True
    tail_is_mm = False
    if 1 <= tail2 <= 12:
        tail_is_mm = True
    result = 'NA'
    if head_is_mm and tail_is_mm:
        result = 'AMBIGUOUS'
    elif head_is_mm:
        result = 'MMYY'
    elif tail_is_mm:
        result = 'YYMM'
    print(result)


if __name__ == '__main__':
    solve()
