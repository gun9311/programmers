#하노이의 탑

def move(no, x, y) :
    if no > 1 :
        move(no-1,x,6-x-y)
