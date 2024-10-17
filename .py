import streamlit as st
import math

# Function definitions for calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return math.pow(x, y)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def logarithm(x, base=10):
    if x <= 0:
        return "Error! Logarithm of non-positive number."
    return math.log(x, base)

# Streamlit app layout
st.title("Scientific Calculator")

# Select operation
operation = st.selectbox("Select operation:", [
    "Add", "Subtract", "Multiply", "Divide", "Power", "Sine", "Cosine", "Tangent", "Logarithm"
])

# Input fields
num1 = st.number_input("Enter first number:", step=0.1)
if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
    num2 = st.number_input("Enter second number:", step=0.1)

# Perform calculations based on selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    elif operation == "Power":
        result = power(num1, num2)
    elif operation == "Sine":
        result = sine(num1)
    elif operation == "Cosine":
        result = cosine(num1)
    elif operation == "Tangent":
        result = tangent(num1)
    elif operation == "Logarithm":
        base = st.number_input("Enter base (default is 10):", value=10, step=1)
        result = logarithm(num1, base)

    # Display result
    st.write(f"Result: {result}")
