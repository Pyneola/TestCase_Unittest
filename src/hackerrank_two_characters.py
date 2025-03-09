def two_characters(s):
    unique_chars = set(s)
    max_length = 0

    if len(unique_chars) < 2:
        return 0

    for char1 in unique_chars:
        for char2 in unique_chars:
            if char1 != char2:
                filtered = [c for c in s if c == char1 or c == char2]

                if len(filtered) <= 2:
                    valid = False
                else:
                    valid = True
                    expected_char = filtered[0]
                    for i in range(1, len(filtered)):
                        expected_char = char1 if expected_char == char2 else char2

                        if filtered[i] != expected_char:
                            valid = False
                            break

                if valid:
                    max_length = max(max_length, len(filtered))

    return max_length
