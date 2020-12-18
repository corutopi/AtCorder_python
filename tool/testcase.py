"""
todo:
    木を返すスニペット
    連結グラフを返すスニペット
    非連結グラフを返すスニペット
"""


def random_str(length, choice=''):
    """指定の長さのランダム英数文字列"""
    from random import choices
    import string
    if choice == '':
        choice = string.ascii_letters + string.digits
    return ''.join(choices(choice, k=length))


def random_ints(num, min, max, duplicate=True, sort=False):
    import random
    import warnings
    ERROR_DOMAIN_NARROW = 'domain error: too narrow domain(min - max) and can\'t take a unique value.'
    WARN_MANY_ELEMENTS = 'too many elements warning: too many elements and it may take a lot of memory.'
    WARN_DOMAIN_NARROW = 'domain of narrow warning: too narrow domain(min - max) and it may take many time of process.'
    element_num = max - min + 1

    if duplicate:
        re = [random.randint(min, max) for _ in range(num)]
    else:
        if num > element_num:
            raise ValueError(ERROR_DOMAIN_NARROW)
        if element_num >= 10 ** 8:
            warnings.warn(WARN_MANY_ELEMENTS, stacklevel=2)
        if num >= 10 ** 6 and element_num / num < 2:
            warnings.warn(WARN_DOMAIN_NARROW, stacklevel=2)

        check = [0] * element_num
        cnt = 0
        re = []
        while cnt < num:
            tmp = random.randint(min, max)
            if check[tmp - min] == 0:
                check[tmp - min] = 1
                cnt += 1
                re.append(tmp)
    if sort:
        re.sort()
    return re


def ppprint(itr_obj):
    if len(itr_obj) == 0:
        print('non list', itr_obj)
    for ite in itr_obj:
        print(ite)


def make_test_graph_data(node, edge, is_directed=False):
    import random
    count = 0
    re = []
    while count < edge:
        new = [random.randint(1, node), random.randint(1, node)]
        if new[0] == new[1]:
            continue
        if not is_directed:
            new.sort()
        if new in re:
            continue
        re.append(new)
        count += 1
    return re
