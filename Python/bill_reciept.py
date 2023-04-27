#order receipt for food item 

def bill_res(type, iname,icost,pieces):
    print("\n\t:::::ORDER RECIEPT::::")
    print("\t=======FREE DELEVERY=======\n\n")
    print("\tfood type= "+type)a
    print("\tfood item= "+iname)
    print("\titem cost= ",icost,"$")
    print("\ttotal bill(in $)= ",icost*pieces)
    print("\ttotal bill(in ₹)= ",icost*pieces*72)

    


print("enter 1.veg Or 2.nonveg =",end="")
type=str(input())

if type=="1":
    type="veg"
    print("\nyou have selected veg as prefrence")
    print("1.dosa=1$\n2.ideli=1.5$\n3.samosa=0.5$\n4.masala dosa=2$")
    item=int(input("? :"))
    if item==1:
        icost=1
        itemname="dosa"
        peices=int(input("enter no of pieces: "))
        bill_res()

    elif item==2:
        icost=1.5
        itemname="ideli"
        peices=int(input("enter no of pieces: "))
        bill_res(type,itemname,icost,peices)

    elif item==3:
        icost=0.5
        itemname="samosa"
        peices=int(input("enter no of pieces: "))
        bill_res(type,itemname,icost,peices)

    elif item==4:
        icost=2
        itemname="masala-dosa"
        peices=int(input("enter no of pieces: "))
        bill_res(type,itemname,icost,peices)
    else:
        print("incorrect choice")

elif type=="2":
    type="nonveg"
    print("\nyou have selected veg as prefrence")
    print("1.lolipop=2$\n2.chicken haka noodle=3$\n3.chicken pizza=7$\n4.masala macchi=5$")
    item=int(input("? :"))
    if item==1:
        icost=2
        itemname="lolipop"
        peices=int(input("enter no of pieces: "))
        bill_res()

    elif item==2:
        icost=3
        itemname="chicken haka noodle"
        peices=int(input("enter no of pieces: "))
        bill_res(type,itemname,icost,peices)

    elif item==3:
        icost=7
        itemname="chicken pizza"
        peices=int(input("enter no of pieces: "))
        bill_res(type,itemname,icost,peices)

    elif item==4:
        icost=5
        itemname="masala macchi"
        peices=int(input("enter no of pieces: "))
        bill_res(type,itemname,icost,peices)
    else:
        print("incorrect choice")
else:
    print("you have selected incorrect choice")

print("\r")
    