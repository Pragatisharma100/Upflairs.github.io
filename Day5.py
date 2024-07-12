# LOOPS....
# n=int(input("Enter the value"))
# for i in range( 0,n):      #(start,stoping,jump)
#     print("Hello world")
#     print(i)

# st="upflairs"
# ls =[10,20,30,40,50,60,70,80,90]
# for item in ls:
#     print(item)
# for item in ls:
#     if(item>50):
#      print(item)

# st= {80,96,46,63,80,20}
# for items in st:
#     print(items)

# dt= {'A':10,"B":20,"C":30,"D":40,"E":50}
# for items in dt.values():
# for items in dt.items():
#     print(items)
# print(dt.items())

# TUPLE UNPACKING.....
# tpl =(10,20)
# a,b =tpl    # same no. of variables should be there for unpacking
# print(a)
# print(b)
# dt= {'A':10,"B":20,"C":30,"D":40,"E":50}
# for items in dt.values():
# for key,values in dt.items():
#     print("key >>>>> ",key,"values >>>>",values)
# print(dt.items())

# ls =[52,65,26,72,63,65,52,2,34,76,98,76,]
# even =0
# odd =0
# for items in ls:
#     if items<50:
#        if(items%2==0):
#         # print("Even")
#         even +=1
#     else:
#         # print("odd")
#         odd +=1

# print("even no. :" ,even)
# print("odd no.:",odd)


# WHILE LOOP
# -> for loop can be performed by while loop but not while loop can performed the for loop work

# i=0
# while(i<=10):  #infinite loop
#     print(i)
#     i+=1

# for i in range(11):
#     print(i)
# condition = True
# while condition:    
#     user_input = input("Do you want to quiet it press Y/y")
#     if user_input =="Y" or user_input =="y":
#         condition = False
#     print("welcome to Upflairs")

# for i in range(100):
#     print(i)
#     if i ==50:
#         break

# for i in range(10):
#     if i ==5:
#         continue
#     print(i)

# count =0
# for i in range(10):
#     count +=1
#     continue
#     print(i)
    
# print(count)   
    
# MAX, MIN......
# ls =[23,45,67,89,98,716,54,32,21,34,67,43,57]
# min(ls) #WAP to find the min element from the given list, without the min function
# max(ls) #WAP to find the max element from the given list, without the max function
# max=ls[0]
# min=ls[0]
# for i in range (len(ls)):
#     if ls[i]>max:
#         max=ls[i]
#     elif ls[i]<min:
#         min=ls[i]
# print("max element in list:" ,max)
# print("min element in list:",min)


# print(min(ls))
# print(max(ls))
    

ls2 = [43,23,4,56,7.5,32.7,35.66,34,20.20,40.40,"upflairs",True]
# integer = 5
# float =5
# string =1
# boolean =1
countInt=0
countFloat =0
countString =0
countBoolean=0
for i in range(len(ls2)):
    if type(ls2[i])==int :
        countInt+=1
    elif type(ls2[i])==float:
        countFloat+=1
    elif type(ls2[i])==str:
        countString+=1
    elif type(ls2[i])==bool:
        countBoolean+=1
print("the integer count is",countInt)
print("the float count is:",countFloat) 
print("the string count is:",countString)
print("the boolean count is:",countBoolean)


    

