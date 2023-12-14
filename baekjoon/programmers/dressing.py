def solution(bandage, health, attacks):
    answer = -1
    max_health = health
    time = attacks[-1][0]+1
    recovery = 0

    for i in range(1,time) :
        attack = False
        for j in range(len(attacks)) :
            if attacks[j][0] == i :                
                health -= attacks[j][1]
                recovery = 0
                attack =True
                break
        if attack == True :
            continue
        recovery += 1
        if recovery == bandage[0] : 
            if health + bandage[1] + bandage[2] <= max_health :
                health += bandage[1] + bandage[2]
            else :
                health = max_health
            recovery = 0
        else:
            if health + bandage[1] <= max_health :
                health += bandage[1]
            else :
                health = max_health 
    if health <=0 :
        return answer
    return health