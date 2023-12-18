from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    line = [[0]*102 for _ in range(102)]
    for i in rectangle :
        for X in range(i[0]*2,(i[2]*2)+1) :
            for Y in range(i[1]*2,(i[3]*2)+1):
                if i[0]*2<X<i[2]*2 and i[1]*2<Y<i[3]*2 :
                    line[X][Y] = -1
                else :
                    if line[X][Y] != -1 :
                        line[X][Y] = 1
    search = deque()
    visited = [[False]*102 for _ in range(102)]
    search.append((characterX*2,characterY*2,answer))
    visited[characterX*2][characterY*2] = True
    
    while search:
        x, y, total  = search.popleft()
        if x == itemX*2 and y == itemY*2 :
            print(total//2)
            return total//2
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx , ny = x +dx , y+dy
            if line[nx][ny] == 1 and visited[nx][ny] == False :
                search.append((nx,ny,total+1))
                visited[nx][ny] = True

rec = [[2,1,7,5],[6,4,10,10]]
solution(rec, 3, 1, 7, 10)