from logic.calculator import add, add_generated_numbers
import sys
# import os
def greeting():
    print("Hello World")
    print(add(1,2))
    print(add_generated_numbers())
    print(sys.path)

if __name__ == '__main__':
    greeting()
