def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a=int(input("enter any number"))
b=int(input("enter any number"))

print('''1. Addition
         2. Subtraction
         3. Multiplication
         4. Division''')
choice=int(input("enter your choice"))

if choice==1:
    print("result", add(a,b))
elif choice==2:
    print("result", sub(a,b))
elif choice==3:
    print("result", mul(a,b))
elif choice==4:
    print("result", div(a,b))
else:
    print("invalid choice")
