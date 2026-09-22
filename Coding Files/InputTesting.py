#Testing Inputs
#input1 = input("Enter a number: ")



def script():
    # program code here...
    input1 = input("Enter a number: ")
    
    restart = input("Would you like to restart this program?")
    if restart == "yes" or restart == "y":
        script()
    if restart == "n" or restart == "no":
        print ("Script terminating. Goodbye.")
script()        
