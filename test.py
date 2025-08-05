print ("Welcome to Ayush ATM")
print ("Insert your ATM card")
pin = int (input ("Enter your pin Number"))
lpin = [1234, 4545,2006,5678,1111,2222,3333,4444]
Amount , DAmount , WAmount = 0.0,0.0,0.0
if pin in lpin :
        while True:
                ch = input ("Select D for Deposite \nSelect W for withdraw \nselect C for Check Current Balance \nSelect Q for Quit from ATM")
                if ch == 'D':
                        DAmount = float (input("Enter Deposite amount"))
                        Amount += DAmount

                elif ch == 'W':
                        WAmount = float (input("Enter Withdraw amount"))
                        if WAmount > Amount:
                                print("Insufficient balance")
                        else:
                                Amount -= WAmount
                                print("Please collect your cash")
                elif ch == 'C':
                        print("your current balance = Rs.",Amount)
                elif ch == 'Q':
                        print ("Thank you \n Visit Next Time")
                        exit ()
                else:
                        print ("invalid choice \n try next time")
                        exit ()

else:
    print ("your pin is invalid \nTry next time")