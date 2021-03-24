def smart_divide(func):
    def inner(a,b):
        print(" I am going to divide a with b")
        if b == 0:
            print("cant divide")
            return
        return func(a,b)
    return inner
@smart_divide
def divide(a,b):
    print(a/b)
divide(45,5)
divide(3,0)