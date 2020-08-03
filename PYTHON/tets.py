for s in[*open(0)][1:]:
    x,y,z=sorted(map(int,s.split()))
    print(*(['YES',x,x,y],['NO'])[z>y])
