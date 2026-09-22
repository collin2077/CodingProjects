#domain = input("Enter the domain name: ")

# def get_domain():
#     while True:
#         if domain == str(domain):
#             print(domain)
#             break
#         else:
#             print("Try again")
#             domain = input("Enter the domain name: ")
#             continue


# Line 15 is the dictionary for Domain Name and Base Login Date
domaindict = { 
    "domain1" : "Tower",
    "last login1" : "2024-06-01",
    #"domain2" : "Waypoint",
    #"last login2" : "2024-06-01 ",
    #"domain3" : "Archer",
    #"last login3" : "2024-06-01",  
}

print_dict_values = domaindict.values() #Print origanal dictionary values to make sure they are correct

print(print_dict_values)

def user_input_for_login(): #collecting Last Login from user input and returning it to be used in the update_last_login function
    domain_input = input("Enter the domain name: ")
    domain_login = input("Enter the last login date and time (YYYY-MM-DD) : " )
    return domain_input, domain_login

user_domain, user_login = user_input_for_login() #Run user input function to get domain and login date

def update_last_login(domain):
    if domain in domaindict:
        domaindict[domain] = user_login  # Update with the user-provided login date and time
        print(f"Last login for {domain} updated.")
    else:
        print(f"{domain} not found in the dictionary.")

update_last_login("domain1")  # Example usage

print(print_dict_values) 