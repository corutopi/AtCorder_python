

def get_divisors(num):
    """
    指定した整数のすべての約数を配列にして返す.

    :param num:
    :return:
    """
    import math
    max_num = math.floor(math.sqrt(num))
    re = set()
    for i in range(1, max_num + 1):
        if num % i == 0:
            re.add(i)
            re.add(num // i)
    return sorted(re)


def solve():
    N = int(input())
    result = 0

    ls = get_divisors(N)

    # x * m == N - y
    # x * m == N - x
    # x * m + x == N
    # (m + 1) * x == N
    for m in ls[1:]:
        m -= 1
        if N // m == N % m:
            result += m
    print(result)


if __name__ == '__main__':
    solve()
