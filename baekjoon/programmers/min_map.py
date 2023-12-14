from collections import deque
def solution(maps):
    answer = 0
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    start = deque()
    
    def bfs():
        nonlocal answer
        while start :
            x,y,score  = start.popleft()
            if x == len(maps)-1 and y == len(maps[0])-1 :
                return score
            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)] :
                nx, ny = x+dx, y+dy
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and visited[nx][ny] == False and maps[nx][ny] == 1 :
                    visited[nx][ny] = True
                    start.append((nx,ny,score+1))
        return -1
        
    start.append((0,0,1))
    visited[0][0] = True
    answer= bfs()
    
    print(answer)
    return answer
map = [[1, 1, 1], [1, 0, 0], [1, 1, 1]]
solution(map)