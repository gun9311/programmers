from collections import deque

def solution(n, computers):
    answer = 0
    computer = deque()
    visited = [False]*len(computers)
    
    def bfs() :
        while computer :
            x = computer.popleft()
            visited[x]  = True
            for j in range(len(computers[x])):
                    if computers[x][j] == 1 and x != j and visited[j] == False:
                        computer.append(j)
    
    for i in range(n) :
        if visited[i] == False :
            computer.append(i)
            bfs()
            answer += 1
    print(answer)
    return answer
c=	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
solution(3, c)