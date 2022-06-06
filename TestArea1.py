for i in range(int(input())):
    x,y=map(int,input().split())
    if x<y:
        g=y*y
        print(g-x+1)
    elif x>y:
        g=x*x
        print(g-y+1)
    else:
        print((x*x)+1)