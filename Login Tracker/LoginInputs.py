domain = input("Enter the domain name: ")

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
    "domain2" : "Waypoint",
    "domain3" : "Archer",
}

get_domain()