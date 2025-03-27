#Herrgott
#1
z=1
x=int(input("Zadejte číslo:"))
y=int(input("Zadejte počet řádků:"))
if y<=0:
    print("Chyba v počtu řádků.")
else:
    for i in range(0,y):
        print(z,"x",x,"=",z*x)
        z+=1




#