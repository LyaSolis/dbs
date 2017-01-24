#Request user input 
while True :
    try :
        name=raw_input('Employee Name: ') 
        name=(name)    
        hours=raw_input('Number of hours worked: ')
        hours=float(hours)       
        rate=raw_input('Hourly Rate: ')
        rate=float(rate)     
        overtime=raw_input('Overtime Rate: ')
        overtime=float(overtime)  
        tax=raw_input('Enter tax rate: ')    
        tax=float(tax)
        tax=(tax/100)
        break 
    except :
        print ('Invalid input')

#computepay function
def computepay() :
    if hours <= 40 :
        gross=hours*rate
        return gross
    elif hours > 40 :
        grossot=(40*rate)+(hours-40)*rate
        return grossot
taxdeduct=tax*computepay()        
gross=computepay() 
netpay=computepay()-taxdeduct
        
#payslip format      
def payslip() :
    print 'Employee Name: ', name 
    print 'Hours worked: ', hours
    print 'Overtime rate: ', overtime
    print 'Gross Pay: ', gross
    print 'Tax Deductions: ', taxdeduct
    print 'Net Pay: ', netpay
    
print payslip()
