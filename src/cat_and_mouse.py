def cat_and_mouse(x, y, z):
    dist_a = abs(z - x)
    dist_b = abs(z - y)
    if dist_a < dist_b:
        return "Cat A"
    elif dist_b < dist_a:
        return "Cat B"
    return "Mouse C"
