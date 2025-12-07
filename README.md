# Calculator
This is a basic calculator program written in Python.  
It performs simple mathematical operations: **Addition, Subtraction, Multiplication, and Division**.

## 🚀 Features
- Add two numbers  
- Subtract two numbers  
- Multiply two numbers  
- Divide two numbers  
- Clean and simple code  
- Beginner-friendly project

## 🧠 Code
~~~python
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

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

✨ Author
Shubh Pandey (Shubh4048)
