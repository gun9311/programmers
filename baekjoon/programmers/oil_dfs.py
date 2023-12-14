def solution(land):
    oils = []
    total = [0]*len(land[0])
    
    for i in range(len(land)) :
        for j in range(len(land[0])):
            if land[i][j] == 1 :
                oils.append((i,j))
    
    visited = [[False]*len(land[0]) for _ in range(len(land))]
    
    def dfs(x,y,point,sichu):
        point += 1
        visited[x][y] = True
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)] :
            nx, ny = x+dx, y+dy
            if 0<=nx<len(land) and 0<=ny<len(land[0]) and  visited[nx][ny] ==False and land[nx][ny] == 1:
                point = dfs(nx,ny,point,sichu)
        sichu[y] = point
        return point
    
    for x,y in oils:
        point = 0
        sichu = [0]*len(land[0])
        if visited[x][y] == False :
            dfs(x,y,point,sichu)
            for i in range(len(land[0])):
                total[i] += sichu[i]
    
    answer = max(total)
    return answer


land =[[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
solution(land)