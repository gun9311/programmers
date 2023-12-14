answer = 1
def solution(n,a,b):
    global answer
    nn = n//2
    if a%2 == 0:
        na = a//2
    else :
        na = a//2 +1
    if b%2 == 0:
        nb = b//2
    else :
        nb = b//2 +1
    if na==nb :
        return answer
    answer += 1
    solution(nn,na,nb)
    return answer