# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 02:24:11 2020

@author: acer
"""

<<<<<<< HEAD
chances = 3
balance = 67.14
while chances >= 0:
    pin = int(input('Please Enter You 4 Digit Pin: '))
    if pin == (1234):
        print('You entered you pin Correctly\n')
        while restart not in ('n','NO','no','N'):
            print('Please Press 1 For Your Balance\n')
            print('Please Press 2 To Make a Withdrawl\n')
            print('Please Press 3 To Pay in\n')
            print('Please Press 4 To Return Card\n')
            option = int(input('What Would you like to choose?'))
            if option == 1:
                print('Your Balance is Â£',balance,'\n')
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How Much Would you like to      
withdraw? \nÂ£10/Â£20/Â£40/Â£60/Â£80/Â£100 for other enter 1: '))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print ('\nYour Balance is now Â£',balance)
                    restart = input('Would You you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Desired amount:'))    
=======
### you can test it, not finished yet

numéros_de_comptes=[23410324,132432,9865665,596900,4654680,76432,86785342,5678888,734533,456045456]
clé_de_comptes=[2344,5433,7523,9806,4560,6454,5343,6565,3455,5677]
solde_de_comptes=[20000,10000,0,0,0,0,0,0,0,0]
>>>>>>> 855376395f94add97b931bf7a9745c1adf73f96d

            elif option == 3:
                Pay_in = float(input('How Much Would You Like To Pay In? '))
                balance = balance + Pay_in
                print ('\nYour Balance is now Â£',balance)
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Please wait whilst your card is Returned...\n')
                print('Thank you for you service')
                break
            else:
                print('Please Enter a correct number. \n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break


    
    
  
