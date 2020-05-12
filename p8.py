lst1 = [2.23, 10,.4,"E ai mano",[10,20],"Vai Corinthians!!!"]

for i in lst1:
    if type(i) == int:
        print(i*2)
    else:
        print(type(i), i)
