def loop_shift(n, s, digit=None):
    """
    n を 2進数表記で s だけ右方向にループさせた結果を返す.
    :param n:
    :param s:
    :param digit:
    :return:
    """
    if digit is None:
        digit = len(bin(n)) - 2
    for _ in range(s):
        d = n & 1
        n = n >> 1
        n += d * 2 ** (digit - 1)
    return n