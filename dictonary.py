mark={'Anurag':49,'Atharv':98,'Priti':76,'Priyanka':79}
x=input("Enter the student's name::")
if mark.get(x):
    print(x,"'s mark is::",mark[x])
else:
    print('Student not found')