def caesar_cipher(s, k):
    result = ""
    for char in s:
        if char.isalpha():
            shift = k % 26
            if char.islower():
                result += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            else:
                result += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        else:
            result += char
    return result
