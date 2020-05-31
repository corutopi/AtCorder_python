# 検証と認識が甘かった


def solve(A, B):
    _B = round(B * 100)
    print(A * _B // 100)


if __name__ == '__main__':
    A, B = [float(i) for i in input().split()]
    A = int(A)
    sorted(A, B)
