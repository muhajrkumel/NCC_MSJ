a,b=input().split ()
w=int(a)
v=int(b)
for i in range(v):
    if w%10==0:
        w=w//10
    else:
        w-=1
print(w)        
