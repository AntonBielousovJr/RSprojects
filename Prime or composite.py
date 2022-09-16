print('''this program will prompt you to input a whole number and will tell you whether
your number is prime or composite.


''')

mode = 1
while mode == 1:
    print(" ")
    print(" ")
    n = int(input("Please pick a whole number : "))
    mode = 0
    f = 1

    if n < 2:
        print("please enter a number greater than 1")
        mode = 1

    else:
        
        while f <= n**(1/2):

                f=f+1
                
                if (n%f) == 0:
                    print("the number", n,"is composite")
                    n = 0
                    mode = 1
                    
                if f >= n**(1/2) and ((n%f) < 0 or (n%f) > 0):
                    print("the number", n,"is prime")
                    mode = 1

