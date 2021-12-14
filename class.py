class MyComplexNumber:
    def __init__(self, real=0, image=0):
        print("MyComplexNumber construction executing...")
        self.real_part = real
        self.image_part = image

    def displayComplex(self):
        print("{0} + {1}j".format(self.real_part, self.image_part))


testing1 = MyComplexNumber(40, 50)
testing1.displayComplex()


class ExampleClass:
    def func1(self):
        print("func1() executing...")

    def func2(self):
        print("func2() execute...")


ob1 = ExampleClass()
ob1.func1()
ob1.func2()

#if
num = 2
if num == 1:
    print("one")
elif num == 2:
    print("tow")
else:
    print("something elese")

#try...raise...catch...finally
try:
    x = 9
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Division Successfully")

finally:
    print("Executing Successfully")
