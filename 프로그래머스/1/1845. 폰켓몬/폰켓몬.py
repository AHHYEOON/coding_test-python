def solution(nums):
    answer = set(nums)
    s = len(nums)/2
    if len(answer) > s:
        return s
    else:
        return len(answer)
    