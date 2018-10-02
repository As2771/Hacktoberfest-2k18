
#function to calculate a factorial of provided number.
def fact(number):
    factorial=1
    while number != 0:
        factorial=factorial*number
        number = number - 1
    return factorial
        

if __name__=="__main__":
    number=int(input("Enter a number:"))
    print("Factorial of provided number : ",fact(number))

