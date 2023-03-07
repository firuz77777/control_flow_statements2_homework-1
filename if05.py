def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a = n % 10
    if n // 10000 > a:
        a = n // 10000
    if n % 10000 // 1000 > a:
        a = n % 10000 // 1000
    if n % 10000 % 1000 // 100 > a:
        a = n % 10000 % 1000 // 100
    if n % 10000 % 1000 % 100 // 10 > a:
        a = n % 10000 % 1000 % 100 // 10
    return a
print(main(12945))