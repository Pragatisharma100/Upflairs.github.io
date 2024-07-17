# ls=[56,24,4,543,32,435,5]
# output=list(map(lambda x:x*x,ls))
# print(output)

# def fun(item):
#     return item**2
# ls= []
# for item in ls:
#     square =fun(item)
#     ls.append(square)

# EXCEPTION HANDLING......
# -> exception is unexpected,unwanted situation
# ->runtime error
# ->compile time error
# -> Error 
# 1. Syntax error
# 2. Type error
# 3. Name error
# 4. Index error



# -> 1.try 
# -> 2.except 
# -> 3.else 
# -> 4.finally

# try:
#     name=input("enter your name:")
#     age=int(input("enter your age:"))
#     print("I am ",name,"and i am ",age ,"year old")
# except:
#     print("Error is occured but don't worry we will execute your remain code")
# else:
#     print("error is not occured")
# finally:
#     print("I will be always")
# print("I am important,plz excute me")

# try:
#     num1=int(input("enter the first number:"))
#     num2=int(input("enter the second number:"))
#     result=num1/num2
#     print(result)
# except ZeroDivisionError:
#     print("don't insert zero in second number")
# except ValueError:
#     print("enter a valid input or integer")

# print("I am important,plz excute me")

# print("hello world")  #compile time error

# ls=[32,5,64,342,435,56,67,45]
# target=3(position)
# postion =return item 
# try:
#     target =int(input("enter your target item:"))
#     position =int(input("enter a position :"))
#     for i in range(len(ls)):
#         if ls[i] == target:
#             print(i)
#             break
#     for i in range(len(ls)):
#         if i==position:
#             print(ls[position])    
#             break
# except ValueError:
#     print("correct the value")
# except IndexError:
#     print("correct the index")

# try:
#     age=int(input("enter age:"))
# except Exception as e:
#     print(e)
# except:
#     print("Error is there")
# except:
#     pass

