from itertools import combinations
def solution(cards1, cards2, goal):
    answer = "Yes"
    comb1 = combinations(cards1,2)
    for i in comb1:
        if i[0] in goal and i[1] in goal :
            number1 = goal.index(i[0])
            number2 = goal.index(i[1])
            if number1 > number2 :
                answer = "No"
                
    comb2 = combinations(cards2,2)
    for j in comb2:
        if j[0] in goal and j[1] in goal :
            number1 = goal.index(j[0])
            number2 = goal.index(j[1])
            if number1 > number2 :
                answer = "No"

    print(answer)
    return answer
    
    # for i in range(len(cards2)-1):
    #     if cards2[i] in goal and cards2[i+1] in goal :
    #         number1 = goal.index(cards2[i])
    #         number2 = goal.index(cards2[i+1])
    #         if number1 > number2 :
    #             answer = "No"

c1 =  ["a", "b", "c"]
c2 = ["d", "e", "f"]
goal =["a", "d", "f"]
solution(c1,c2,goal)