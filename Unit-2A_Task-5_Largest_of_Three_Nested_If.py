# largest of three number using nested if .
p=int(input("Enter first number:"))
q=int(input("Enter second number:"))
r=int(input("Enter third number:"))
if p>=q:
    if p>=r:
        largest =p
    else:
        largest =r
else:
    if q>=r:
        largest =q
    else:
        largest =r
print("largest number is:",largest)
