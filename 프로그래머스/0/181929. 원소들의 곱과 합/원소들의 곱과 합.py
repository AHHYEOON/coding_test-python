def solution(num_list):
    s = 0
    r = 1
    for i in num_list:
        s += i
        r *= i
        
    
    return 1 if r < (s**2) else 0