class MyComplexNumber:
    def __init__(self, real=0, image=0):
        print("MyComplexNumber construction executing...")
        self.real_part = real
        self.image_part = image

    def displayComplex(self):
        print("{0} + {1}j".format(self.real_part, self.image_part))


testing1 = MyComplexNumber(40, 50)
testing1.displayComplex()
