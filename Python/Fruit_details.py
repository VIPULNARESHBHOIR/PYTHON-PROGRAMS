class Fruit:
    def __init__(self,color,name,prize):
            self.name=name
            self.color=color
            self.prize=prize
    
    def details(self):
        print("\nname:",self.name)
        print("color:",self.color)
        print("prize/kg:",self.prize,"$")
        
F1=Fruit( 'red','apple',200 )
F2=Fruit( 'green','apple',150 )
F3=Fruit( 'blue','jamun',180 )
F4=Fruit( 'yellow','banana',100 )
F5=Fruit( 'green','banana',80 )
F6=Fruit( 'yellow','mango',300 )
F7=Fruit( 'green','mango',160 )
F8=Fruit( 'red','stawberry',500)
F9=Fruit( 'red','cherry',400)
F10=Fruit( 'yellow','pineapple',350)
a=int(input("enter choice:1-app,2-ban,3-jamn,4-cherry,5-pineapple,6-stawberry,7-mango:"))

if a==1:
    F1.details()
    F2.details()
if a==2: 
    F4.details()
    F5.details()
if a==3:
    F3.details()
if a==4:
    F9.details()
if a==5:
     F10.details()
if a==6:
     F8.details()
if a==7:
     F7.details()
     F6.details()
