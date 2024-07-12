ls =[245,56,67,43,32,768,42,56,87,89]
# ls=[422,87,65,43,29,10,26,39]
def apan_min(ls):
    min=ls[0]
    for i in range (len(ls)):
        if min>ls[i]:
            min=ls[i]
    return min
# print(apan_min(ls))

def apan_max(ls):
   max=ls[0]
   for i in range(len(ls)):
       if ls[i]>max:
           max=ls[i]
   return max
# print(apan_max(ls))
def sorting(ls):
    for i in range(len(ls)-1):
        min =ls[i]
        k=i
        for j in range(i+1,len(ls)):
            if ls[j]< min:
                min =ls[j]
                k=j
        temp=ls[i]
        ls[i]=ls[k]
        ls[k]=temp
    return ls