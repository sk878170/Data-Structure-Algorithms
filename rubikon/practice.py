a=5
for i in range(1,a+1):
    print(" *"*i+"  "*((a-i)*2)+" *"*i,"* "*(i-1)+"  "*((a-i)*2)+"* "*i)
print(" *"*((a*4)-1))
print(" *"*((a*4)-1))
for i in range(a,0,-1):
    print(" *"*i+"  "*((a-i)*2)+" *"*i,"* "*(i-1)+"  "*((a-i)*2)+"* "*i)