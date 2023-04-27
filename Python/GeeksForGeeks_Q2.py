class Solution:
    def removeReverse(self, S): 
        #code here
        str1=S
        for i in range (len(str1)):
            count=0
            print(len(str1))
            target=str1[i]
            print(target)
            for j in range (len(str1)):
                if str1[j]==target:
                    count+=1
                    if count==1:
                        index1=j
                    if count==2:
                        str1=str1.replace(str1[index1],"",1)
                        str1=str1[::-1]
                        print(str1)
                        break
        return str1

S="lmppp"
obj=Solution()
ans=obj.removeReverse(S)
print(ans)
