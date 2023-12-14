from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    line = [[0]*51 for _ in range(51)]
    for i in rectangle :
        for X in [i[0],i[2]] :
            for Y in range(i[1],i[3]+1):
                line[X][Y] += 1
    # print(line)
    
    search = deque()
    visited = [[False]*51 for _ in range(51)]
    search.append((characterX,characterY,answer))
    visited[characterX][characterY] = True
    
    while search:
        x, y, total  = search.popleft()
        if x == itemX and y == itemY :
            break
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx , ny = x +dx , y+dy
            if line[nx][ny] == 1 and visited[nx][ny] == False :
                search.append((nx,ny,total+1))
                visited[nx][ny] = True
    
    print(total)
    return total


rec = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
solution(rec, 9, 7, 6, 1)