
#request user input
while True:
    try:
        inp=raw_input('Enter number: ')
        if inp=='done': break
        num1=float(inp)
        sum=raw_input('Enter required action: +, -, * or / ')
        inp=raw_input('Enter another number: ')
        num2=float(inp)  
    except:
        print ('Error. Please enter number')
#do computation and return value   
    try:
        if sum=='+':
            print num1+num2
        elif sum=='-':
            print num1-num2
        elif sum=='*':
            print num1*num2
        elif sum=='/':
            print num1/num2 
        else:
            print ('The operation command you entered is not recognised, please enter +, -, * or /')
    except:
        continue 