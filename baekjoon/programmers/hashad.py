def solution(x):
    answer = True
    str_x = str(x)
    result = 0
    for i in range(len(str_x)) :
        result += int(str_x[i])
        
    if x % result != 0 :
        answer = False
    print(answer)
    return answer

x = 11
solution(x)