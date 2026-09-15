def get_domain():
    while True:
        domain = input("Enter the domain name: ")
        if domain != "":
            print(domain)
            return domain
        print("No domain name entered.")
