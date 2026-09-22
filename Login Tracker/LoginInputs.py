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

#print(print_dict_values)

def user_input_for_domain_update(): #collecting Last Login from user input and returning it to be used in the update_last_login function
    input_domain_selection = input("Enter the domain name: ")
    return input_domain_selection

def user_input_for_login():
    input_user_updates_domain_login = input("Enter the last login date and time (YYYY-MM-DD) : " )
    return input_user_updates_domain_login

user_domain_select = user_input_for_domain_update() #Run user input function to get domain


print("MAKE THIS A WHILE TRUE LOOP")
# if user_domain_select in domaindict.values(): #Check if the user input domain is in the dictionary and print a message
#     print(f"{user_domain_select} is in the dictionary.")
# else:
#     print(f"{user_domain_select} is not in the dictionary.")
#     user_domain_select = user_input_for_domain_update() #Run user input function to get domain again

def update_last_login(domain):
    if domain in domaindict:
        domaindict[domain] = user_input_for_login()  # Update with the user-provided login date and time
        print(f"Last login for {domain} updated.")
    else:
        print(f"{domain} not found in the dictionary.")

update_last_login(user_domain_select)# Example usage

print(print_dict_values)