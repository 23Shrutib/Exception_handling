#Exception Handling

'''
try:
    n=int(input("Enter Number "))
    print(10/n)
except ValueError:
    print("please enter number")
except ZeroDivisionError:
    print("plz enter non-zero value")
'''


'''
try:
    n=int(input("enter number "))
    print(10/n)
except Exception as e:
    print(e)
'''


try:
    n=int(input("enter number "))
    print(10/n)
except Exception as e:
    print(e)
else:
    print("else")
finally:
    print("finally")
