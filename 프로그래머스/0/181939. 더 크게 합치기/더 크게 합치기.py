def solution(a, b):
    str_a = str(a)
    str_b = str(b)
    result1 = str_a + str_b
    result2 = str_b + str_a
    if result1 >= result2:
        return int(result1)
    else:
        return int(result2)
  