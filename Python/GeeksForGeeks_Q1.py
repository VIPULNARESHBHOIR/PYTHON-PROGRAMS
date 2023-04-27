#User function Template for python3

class Solution:
    def solve(self,N,arr):
        #code here
        temp=0
        for i in range (N):
            temp=temp+arr[i]
        if temp==0:
            return 'YES'
        else:
            for i in range (N):
                temp=0
                arr[i]=-(arr[i])
                for j in range (N):
                    temp=temp+arr[j]
                if temp==0:
                    return 'YES'
                else:
                    arr[i]=-(arr[i])
                    continue
            if (temp!=0):
                return 'NO'

    
n=int(input("lenght of aaray:"))
arr=list(map(int,input("elements of array:-").split()))
s=Solution()
output=s.solve(n,arr)
print(output)
