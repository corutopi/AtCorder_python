# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(a, b, x):
    import math
    LOOP = 100
    water_max = a ** 2 * b
    area_x = x / a
    half_angle = math.degrees(math.acos(a / math.sqrt(a ** 2 + b ** 2)))
    ans = 0
    if x > water_max / 2:
        top = half_angle
        btm = 0
        for _ in range(LOOP):
            ans = (top + btm) / 2
            angle_a = 90 - ans
            angle_b = ans
            angle_c = 90
            side_a = a  # ★
            side_c = a / math.cos(math.radians(angle_b))
            side_b = side_c * math.sin(math.radians(angle_b))  # ★
            area = side_a * side_b / 2 + side_a * (b - side_b)
            if area >= area_x:
                btm = ans
            else:
                top = ans
    else:
        top = 90
        btm = half_angle
        for _ in range(LOOP):
            ans = (top + btm) / 2
            angle_a = 90 - ans
            angle_b = ans
            angle_c = 90
            side_b = b  # ★
            side_c = b / math.sin(math.radians(angle_b))
            side_a = side_c * math.cos(math.radians(angle_b))  # ★
            area = side_a * side_b / 2
            if area >= area_x:
                btm = ans
            else:
                top = ans

    print(ans)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    a, b, x = map(int, input().split())
    # As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(a, b, x)
