def solve():
    A, B, C, D, E, F = map(int, input().split())
    A, B = 100 * A, 100 * B
    waters = set()
    sugars = set()
    for i in range(3001):
        for j in range(3001):
            if A * i + B * j <= F:
                waters.add(A * i + B * j)
            if C * i + D * j <= F:
                sugars.add(C * i + D * j)
    ans_per = 0
    ans_water = 0
    ans_sugar = 0
    for w in waters:
        if w == 0:
            continue
        for s in sugars:
            if w + s <= F and ans_per <= s / w <= E / 100:
                ans_per = s / w
                ans_water = w
                ans_sugar = s
    print(ans_water + ans_sugar, ans_sugar)


if __name__ == '__main__':
    import datetime
    # print(datetime.datetime.now())
    solve()
    # print(datetime.datetime.now())
