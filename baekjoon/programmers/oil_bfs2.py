from collections import deque

def solution(land):
    answer = 0
    result = [0]*len(land[0])
    oils = deque()
    visited = [[False]*len(land[0]) for _ in range(len(land))]
    
    def bfs() :
        lines = set()
        chunk = 0
        while oils :
            x,y = oils.popleft()
            lines.add(y)
            chunk += 1
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<len(land) and 0<=ny<len(land[0]) and visited[nx][ny] == False and land[nx][ny] == 1 :
                    oils.append((nx,ny))
                    visited[nx][ny] = True
        for line in lines:
            result[line] += chunk
            
    for j in range(len(land[0])):
        for i in range(len(land)):
            if land[i][j] == 1 and visited[i][j] == False :
                oils.append((i,j))
                visited[i][j] = True
                bfs()

    answer = max(result)
    return answer

land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
solution(land)