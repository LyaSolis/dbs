
#Define variables
small = None
countsmall = None
large = None
countlarge = None
print('You will be asked to enter numbers, to carry out computation - please enter 0 ')
#Carry out computation
while True:
    try:
        num = raw_input('Enter a number ')
        num = int(num)
        if num == 0 :
            break
        if large is None or num > large :
            large = num
            countlarge = 1
        elif num == large :
            countlarge = countlarge + 1
        if small is None or num < small :
            small = num
            countsmall = 1
        elif num == small :
            countsmall = countsmall + 1
    except:
        print 'Error. Please enter an integer number.'
#return value        
print 'Largest Number Entered: ', large
print 'Occurences of largest number: ', countlarge
print 'Smallest Number Entered: ', small
print 'Occurences of smallest number: ', countsmall