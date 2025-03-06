def two_characters(s):
    unique_chars = set(s)
    max_length = 0
    for a in unique_chars:
        for b in unique_chars:
            if a != b:
                filtered = [c for c in s if c in (a, b)]
                if all(
                    filtered[i] != filtered[i + 1] for i in range(len(filtered) - 1)
                ):
                    max_length = max(max_length, len(filtered))
    return max_length
