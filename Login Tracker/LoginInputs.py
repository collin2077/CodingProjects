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

domain = {
    "domain1" : "Tower",
    "last login1" : "2024-06-01 12:00:00",
    "domain2" : "Waypoint",
    "last login2" : "2024-06-01 12:00:00",
    "domain3" : "Archer",
    "last login3" : "2024-06-01 12:00:00",  
}

x = domain.get("domain1")
print(x)