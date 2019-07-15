
def solve():
    N = int(input())
    # すべてのAの約数を求める.
    all_divisor = {1}
    divisors = [1] * N
    for i, Ai in enumerate([int(i) for i in input().split()]):
        divisors[i] = get_divisors(Ai)
        pass
    # # この時すべての数の約数の種類を記録しておく
    # 約数の数が N - 1 以下となる数を探す.
    pass


def get_divisors(Ai, x=1, now_result=[1]):
    result = now_result
    for i
    pass


if __name__ == '__main__':
    solve()
