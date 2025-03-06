def is_prime_list(numbers):
    if not numbers:
        return False
    for num in numbers:
        if num < 2:
            return False
        for n in range(2, int(num**0.5) + 1):
            if num % n == 0:
                return False
    return True
