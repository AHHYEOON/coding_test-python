def solution(code):
    mode = 0
    ret = []
    for i in range(len(code)):
        if mode == 0:
            if code[i] != '1':
                if i % 2 == 0:
                    ret.append(code[i])
            else: mode = 1
        else :
            if code[i] != '1':
                if i % 2 :
                    ret.append(code[i])
            else : mode = 0
                    
    answer = "".join(ret)
    
    return answer if ret != [] else 'EMPTY'