class Calculator:
    def calculation_type(self):
        return "Arithmetic Operations"
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        return a * b
    print(f"{calculation_type()}")
    print(f"The product is: {multiply()}")
    
    