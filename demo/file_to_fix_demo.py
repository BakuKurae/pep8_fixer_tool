# Demo Python File with PEP 8 Violations

def bad_function(x):
    y=x*2
    if y>10:
        print("Result is greater than 10.")
    else:
        print("Result is less than or equal to 10.")
        
class BadClass:
    def __init__(self, name):
        self.name=name

    def display_info(self):
        print(f"Name:{self.name}")

def main():
    obj=BadClass("Demo")
    obj.display_info()
    
if __name__ == "__main__":
    main()
