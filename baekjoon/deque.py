from collections import deque

S = list(map(int,(input().split())))
N = S[0]
K = S[1]

people = []
for i in range (1, N+1):
    people.append(i)
    
result=[]

def kill(K) :
    queue = deque(people)
    while len(queue) != 1 :
        for i in range(K-1) :
            queue.append(queue.popleft())
        result.append(queue.popleft())
    result.append(queue.pop())
    return
    
    
kill(K)
for i in range(N) :
    if i==0 :
        print('<',end='')
        
    if i==N-1 :
        print(result[i], '>',  sep='')
    else:
        print(result[i], end=", ")
    