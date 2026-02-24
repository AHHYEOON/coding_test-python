def solution(num_list):
    s,r ='0','0'
    for i in num_list:
        if i % 2 :
            s += str(i)
        else : 
            r += str(i)
    return(int(s)+int(r))