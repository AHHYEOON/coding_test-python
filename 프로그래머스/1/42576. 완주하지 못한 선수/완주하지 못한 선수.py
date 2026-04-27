def solution(participant, completion):
    count = {}
    for name in participant:
        count[name] = count.get(name,0) + 1
    for name in completion:
        count[name] -= 1
    for key, value in count.items():
        if value == 1:
            return key
    
  