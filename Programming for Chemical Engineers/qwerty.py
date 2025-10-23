#Applications of brackets
# [] is used for list; () is used for tuple;
# {} is used for set
x=[94,94,96,97]
y=(95,94,96,97,100)
z={94,95,94,97,94,99}
#print(x)
#print(y)
#print(z)
#print(y[0])
#print(y[-1])
#print(x[0:2])
#for answers in x:
    #print(answers)
x.append(98)
#print(x)
x.insert(1,95)
#print(x)
x.remove(94)
#print(x)
#print(x.count(95))
#print(y.count(95))
#print(x.index(95))
#print(y.index(95))
c=len(x)
#print(c)
#x.clear()
print(x)
for answers in x:
    print(answers)
    if answers == 96:
        break

#Dictionary
age={"1991":23,"1993":25}
#print(age["1991"])
age["1995"]=27
print(age)


