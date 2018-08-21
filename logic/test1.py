def ref_demo(x):
    print "x=",x," id=",id(x)
    x=42
    print "x=",x," id=",id(x)

ref_demo(4)
