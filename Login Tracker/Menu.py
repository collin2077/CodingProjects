# Menu Selection

def add_domain():
    domain_name = input("Please enter the domain name to add: ")
    print("Domain added: "domain_name")

def menu_selection():
    print("Menu Selection")
    menu = {}
    menu['1'] = "Add Domain"
    menu['2'] = "Delete Domain"
    menu['3'] = "Check Last Login"
    menu['4'] = "Exit"

add_domain()