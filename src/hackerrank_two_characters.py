from itertools import combinations


def validate(s):
    for ind in range(len(s) - 1):
        if s[ind] == s[ind + 1]:
            return False
    return True


def two_characters(s):
    str_set = set(list(s))
    variants = combinations(str_set, 2)
    max_res = 0

    for comb in variants:
        t = [c for c in s if c == comb[0] or c == comb[1]]
        if validate(t):
            max_res = max(max_res, len(t))

    return max_res
