def chnage(a,b):
    print("\ni am in change function")
    if a<b:
        m=int((a+b))/2
        chnage(a,m)
        print(f"first value of {m}")
        chnage(m+1,b)
        print(f"second value of {m}")
        ch()
        print("\nend of the func")

def ch():
    print("\ni am in ch function")


chnage(0,8)