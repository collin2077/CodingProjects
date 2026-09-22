#domain = input("Enter the domain name: ")

def get_domain():
    while True:
        if domain == str(domain):
            print(domain)
            break
        else:
            print("Try again")
            domain = input("Enter the domain name: ")
            continue

domaindict = {
    "domain1" : "Tower",
    "last login1" : "2024-06-01 12:00:00",
    #"domain2" : "Waypoint",
    #"last login2" : "2024-06-01 12:00:00",
    #"domain3" : "Archer",
    #"last login3" : "2024-06-01 12:00:00",  
}

x = domaindict.values()

print(x)

def update_last_login(domain):
    if domain in domaindict:
        domaindict[domain] = "2025-12-01"  # Update with the current date and time
        print(f"Last login for {domain} updated.")
    else:
        print(f"{domain} not found in the dictionary.")

update_last_login("domain1")  # Example usage

print(x) 