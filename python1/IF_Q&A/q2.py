'''2: Multiple conditions'''
# Students result with grade
# Modify the earlier program students’ grades in such a way that they should take in five subject marks. Find the total mark and their percentage. Your program should check for the following conditions:
# If the percentage falls below 45, they are considered fail.
# If the percentage is between 45 and 60, grade them as pass.
# If the percentage is between 60 and 75, grade them as good.
# If the percentage is between 75 and 85, grade them as very good.
# If the percentage is between 85 and 100, grade them excellent.
# If the percentage is below zero or above 100, it’s an error.

sub1=int(input("Enter the Mark He got in maths: "))
tot1=int(input("Enter the Total mark of maths:"))
sub2=int(input("Enter the Mark He got in physics: "))
tot2=int(input("Enter the Total mark of  physics:"))
sub3=int(input("Enter the Mark He got in chemistry: "))
tot3=int(input("Enter the Total mark of  chmistry:")) 
sub3=int(input("Enter the Mark He got in chemistry: "))
tot3=int(input("Enter the Total mark of  chmistry:"))
sub4=int(input("Enter the Mark He got in biology: "))
tot4=int(input("Enter the Total mark of  biology:"))
sub5=int(input("Enter the Mark He got in English: "))
tot5=int(input("Enter the Total mark of  English:"))
sum1=sub1+sub2+sub3+sub4+sub5
sum2=tot1+tot2+tot3+tot4+tot5
per=(sum1/sum2)*100
print("Total Mark of the student is :",sum1)
print("Total perentage of the student is :",per)
if per>=85:
    print("grade of the student is excellent")
elif per>=75:
    print("grade them as very good.")
elif per>=60:
    print(" grade them as good")
elif per>=45:
    print("grade them as pass.")
elif per>=0:
    print("they are considered fail.")
else:
    print("error")