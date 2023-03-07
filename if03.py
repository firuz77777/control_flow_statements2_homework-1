def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """ 
    aa = 0
    mx = a
    if mx < b:
        mx = b
    if mx < c:
        mx = c
    mm = a
    if mm > b:
        mm = b
    if mm > c:
        mm = c
    if mx > a > mm:
        aa = a
    if mx > b > mm:
        aa = b
    if mx > c > mm:
        aa = c
    return aa
print(main(3,9,4))