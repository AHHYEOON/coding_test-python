def solution(n):
    sum = 0
    answer = 0
    if n % 2 == 1:
        for i in range(n+1):
            if i % 2 == 1:
                answer += i
    else :
        for i in range(n+1):
            if i % 2 == 0:
                r = i*i
                answer += r
    return answer