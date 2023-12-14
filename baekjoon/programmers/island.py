def solution(maps):
    answer = []
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    q = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" :
                q.append((i,j))
            else :
                visited[i][j] = True
    
    def dfs(x,y,total):
        visited[x][y] = True
        total += int(maps[x][y])
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)] :
            nx, ny = x+dx, y+dy
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and visited[nx][ny] == False:
                total = dfs(nx,ny,total)
        return total
    
    for x,y in q :            
        result = 0
        if visited[x][y] == False :
            answer.append(dfs(x,y,result))
    if answer :
        return sorted(answer)
    else :
        return [-1]







# list = []

# def dfs(maps, x,y,visted):
#     global list
#     visted[x][y] = True
#     for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
#         nx,ny = x+dx, y+dy 
#         if visted[nx][ny] == False and 0<=nx<len(maps) and 0<=ny<len(maps[0]) :
#             list.append((nx,ny))
#             visted[nx][ny] = True
#             dfs(maps, nx, ny, visted)
#         return
#     return list
    

# def solution(maps):
#     result = 0 
#     answer = [] 
#     visited = [[False]*len(i) for i in maps]
#     for i in(range(len(maps))):
#         for j in range(len(maps[0])):
#             if visited[i][j] == False and maps[i][j] != "X": 
#                 for x,y in dfs(maps,i,j,visited):
#                     result += maps[x][y]
#                     answer.append(result)
#     answer.sort
#     return answer

# maps = ["X591X","X1X5X","X231X", "1XXX1"]
# print(solution(maps))

