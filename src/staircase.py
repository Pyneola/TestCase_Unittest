def staircase(n, pattern="#"):
    return "\n".join((" " * (n - i - 1) + pattern * (i + 1)) for i in range(n))
