from collections import Counter

def solution(participant, completion):
    answer = ''
    c_part = Counter(participant)
    c_comp = Counter(completion)
    # c_part.subtract(c_comp)
    # answer = answer.join(c_part.elements())
    for i in c_part :
        if c_part[i] != c_comp[i]:    
            print (i)
            return i

p = ["leo", "kiki", "eden"]
c = ["eden", "kiki"]
solution(p,c)