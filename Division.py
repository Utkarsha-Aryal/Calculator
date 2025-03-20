# Division.py
class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def divide_numbers(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return "Error! Division by zero is not allowed."