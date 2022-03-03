def name(heads, legs):
    chicken=0
    rabbit=0
    if heads>=legs or legs%2!=0:
        print("No solution")
    else:
        rabbit=(legs-2*heads)/2   #C+R=35, 2C+4R=94 --> 2C+2R=70-->2C=70-2R --> 70-2R+4R=94--> 2R=94-2*35--> R=(94-2*35)/2
        chicken=heads-rabbit
