#list
a = [1,2,3]
print(a)
b = list((4,5,6))
print(b)
c = list(range(1,11))
print(c)
d = [x*x for x in range(11)]
print(d)
e = []
f = list()
print(e, f)
g = list("hey jasmitha")
print(g) 
a = [1,2,3,4,5]
b = [6,7,8,9,0]
print("add: ",a + b)
print("mul: ",a*3)
print("scl:",a[0:3])
del a[2]
print("del",a)

#list comprehension inventory management
items = ["apple", "banana", "orange", "mango", "pen", "pencil", "marker", "papers", "glue"]
qty = [40,4,3,20,5,44,2,6,8]
low_stock = [items[i] for i in range(len(items)) if qty[i]<10]
print(low_stock)

#even or odd
num = int(input("enter a number:"))
if num %2==0 :
    print("number is even")
else:
    print("numer is odd")

    #grade using elif
marks = int(input("enter marks of student:"))
if marks > 90:
    print("GRADE A")
elif marks >= 80:
    print("GRADE B")
elif marks >= 70:
    print("GRADE C")
elif marks >= 60:
    print("GRADE D")
else:
    print("GRADE F")

#largest of three numbers
a = int(input("enter a first number:"))
b = int(input("enter a second number:"))
c = int(input("enter a third number:"))
if a>=b and a>=c:
    print("largest number is:", a)
elif b>=a and b>=c:
    print("largest number is:", b)
else:
    print("largest number is:", c)

n = int(input("Enter n: "))
