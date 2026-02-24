def solution(a, b, c):
    if a != b :
        if a == c :
            return (a + b + c) * (a*a + b*b + c*c)
        elif b == c :
            return (a + b + c) * (a*a + b*b + c*c)
        else :
            return a + b + c
    else :
        if a != c :
            return (a + b + c) * (a*a + b*b + c*c)
        else :
            return (a + b + c ) * (a*a + b*b + c*c) * (a**3 + b**3 + c**3)
        