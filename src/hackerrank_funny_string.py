def funny_string(s):
    r = s[::-1]

    s_diff = []
    r_diff = []

    for i in range(1, len(s)):
        s_diff.append(abs(ord(s[i]) - ord(s[i - 1])))
        r_diff.append(abs(ord(r[i]) - ord(r[i - 1])))

    if s_diff == r_diff:
        return "Funny"
    else:
        return "Not Funny"
