"""
循环和递归可以互相替换
"""

def Prints(number):
    i=0
    if number!=i:
        print(number)
        Prints(number-1)

if __name__ == '__main__':
    Prints(100)