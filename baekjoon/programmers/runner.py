def solution(participant, completion):
    answer = ''
    for i in completion :
        if i in participant :
            participant.remove(i)
    for i in participant :
        answer = i
    print (answer)
    return answer

p = ["leo", "kiki", "eden"]
c = ["eden", "kiki"]
solution(p,c)