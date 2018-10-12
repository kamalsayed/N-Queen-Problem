

if __name__ == '__main__':
    pass
    factor=1
    n = 7
    for i in range(1,n +1):
        factor=factor*i        
    print(factor)
def fact(n): #functional
        if n==1:
            return n
        else:
            return n*fact(n-1)
     
print(fact(7)) # call the fact function

class Factorial_class(): #class fashion
    def __init__(self, number):
        self.number = number
        factorial=1
        for i in range(1,number +1):
            factorial=factorial*i 
        print(factorial)  
        
oopfact = Factorial_class(number = 7) #object to use factorial class



