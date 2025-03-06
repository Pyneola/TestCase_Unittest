def funny_string(s):
    return (
        "Funny"
        if list(map(abs, [ord(s[i]) - ord(s[i - 1]) for i in range(1, len(s))]))
        == list(map(abs, [ord(s[-i]) - ord(s[-i - 1]) for i in range(1, len(s))]))
        else "Not Funny"
    )
