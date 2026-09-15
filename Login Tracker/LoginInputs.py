Domain1 = str(input("Enter the domain name: "))

while True:
    if Domain1 != "":
        print(Domain1)
        break
    else:
        print("No domain name entered.")
        Domain1 = str(input("Enter the domain name: "))
        continue