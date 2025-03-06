def funny_string(s):
    reverse = [ord(letter) for letter in list(reversed(s))]
    s = [ord(letter) for letter in s]
    r = [abs(reverse[i] - reverse[i + 1]) for i in range(len(reverse) - 1)]
    s = [abs(s[i] - s[i + 1]) for i in range(len(reverse) - 1)]
    if r == s:
        return "Funny"
    return "Not Funny"
