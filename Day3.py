#int,float,string,list,bool

# TUPLE......
# ->IMUTUABLE UNCHANGABLE
# ->INSERT,DELETE NO
# tpl = (14.25,"upflairs",True)
# print(tpl)
# print(type(tpl))

# INDEX,COUNT........
# tpl = (14.25,"upflairs",True)
# tpl =('A','B','C','A','B')
# print(tpl.count('B'))
# print(tpl.index('C'))
# tpl[2]="jaipur"
# del tpl[2]
# print(tpl)

# tpl =("a",)
# print(type(tpl))
# tpl ='A','B','C','A','B'
# tpl2 ="A",
# print(type(tpl))
# print(type(tpl2))

# SET........
# ->IMMUTABLE
# ->DOESNOT ALLOW THE DUPLICATE ITEMS
# ->INDEXING NOT ALLOW
# ->INSERT, DELETE,YES


# st ={1,1,2,2,3,3,4,5,6,7}
# print(st)
# print(type(st))

# st ={85,45,69,85,2,14,52,63,73}
# print(st[2])

# INSERT.......
# st.add(1000)
# st.remove(85)
# st.discard(85) #items remove
# print(st)

# UPDATE,INTERSECTION......
# st1 ={85,45,69,85,2,14,52,63,73}
# st2 ={85,45,69,2000}
# st1.update(st2)
# print(st1)
# print(st1.intersection(st2))

# TYPECASTING.....
# var =10.23
# var =int(var)
# print(type(var))
# print(var)

# ls =[25,41,63,96,85]
# ls =set(ls)
# print(ls)
# print(type(ls))

# ls=[11,22,11,22,44,11,55]
# ls =list(set(ls))
# print(ls)

# DICTIONARY.......
# ->KEY:VALUE --> PAIRS
# ->INDEX VALUE IS NOT ASSINGED
# ->MUTUABLE
# ->CHANGE ALLOWED IN DICTIONARY

# st={0:10,1:20,2:30}
# print(st)
# print(type(st))

# dt={'A':100,'B':200,'C':300,'A':1000}
# print(dt)

# dt={'A':100,'B':200,'C':300}
# dt2={'E':500}
# dt['B']=500
# dt['D']=500
# dt.pop('A')
# print(dt.keys())
# print(dt.values())
# dt.update(dt2)
# print(dt)

# name ,marks,subject
# student_name={"Name":["Nikita","pragati","arushi"],
#               "Marks":[52,41,96],
#               "Subject":"math"}

# student_name["Name"].append("Boss")
# print(student_name)
# print(student_name["Name"],student_name["Marks"])
# student_name["Name"].insert(0,"Pragati")
# print(student_name)
# print(type(student_name))

# student_name["Name"][1]="ketan"
# print(student_name)

# print("HELLO WORLD")
# print("HELLO WORLD")
# print("HELLO WORLD")

