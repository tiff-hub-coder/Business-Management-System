# ============================================= STORAGE ============================================

main_menu_options = [
    "Client Administration",
    "Open Client Workspace",
    "Save Data",
    "Exit"
]

admin_menu_options = [
    "Register Client",
    "View Clients",
    "Search Client",
    "Edit Client",
    "Delete Client",
    "Save",
    "Return to Main Menu"
]

workspace_menu_options = [
    "Customer Management",
    "Employee Management",
    "Supplier Management",
    "Offerings",
    "Sales & Transactions",
    "Financial Management",
    "Reports",
    "Analytics Centre",
    "Switch Client",
    "Return to Main Menu"
]

active_client = None

# ============================================= MAIN ============================================

def main():
    while True:
        display_menu(
            'BUSINESS MANAGEMENT & ANALYTICS SYSTEM',
            main_menu_options
        )
        chosen_main_option = get_menu_choice(
            "Choose a main menu option: ",
            main_menu_options
        )

        if chosen_main_option == 1:
            admin_menu()
        elif chosen_main_option == 2:
            workspace_menu()
        elif chosen_main_option == 3:
            save_option()
        elif chosen_main_option == 4:
            exit_option()
            break


# ============================================= DISPLAY MENU FUNCTION ============================================

def display_menu(title, menu_options):

    print("=" * 50)
    print(title)
    print("=" * 50)
    print(f"Active Client: {active_client}")
    print("=" * 50)

    for number, option in enumerate(menu_options, start=1):
        print(f"{number}. {option}")

# ============================================= GET CHOICE FUNCTION ============================================

def get_menu_choice(prompt, menu_options):
    while True:
        try:
            choice = int(input(prompt))
        except ValueError:
            print("Please enter a valid number. ")
            continue
        if choice < 1 or choice > len(menu_options):
            print("Invalid Entry ")
            continue
        return choice

# ============================================= SAVE FUNCTION ============================================

def save_option():
    print("Save feature coming in Version 3.")

# ============================================= EXIT FUNCTION ============================================

def exit_option():
    print("Exiting...")

# ============================================= ADMIN MENU ============================================

def admin_menu():

    while True:
        display_menu(
            "CLIENT ADMINSTRATION",
            admin_menu_options
        )
        chosen_admin_option = get_menu_choice(
            "Choose an administration option: ",
            admin_menu_options
        )
        if chosen_admin_option == 1:
            register_client()
        elif chosen_admin_option == 2:
            view_clients()
        elif chosen_admin_option == 3:
            search_client()
        elif chosen_admin_option == 4:
            edit_client()
        elif chosen_admin_option == 5:
            delete_client()    
        elif chosen_admin_option == 6:
           save_option()
        elif chosen_admin_option == 7:
            print("Returning to main menu...")
            break

# ============================================= WORKSPACE MENU ============================================
def workspace_menu():
    while True:
        display_menu(
            "CLIENT WORKSPACE",
            workspace_menu_options
        )
        chosen_workspace_option = get_menu_choice(
            "Choose a workspace option: ",
            workspace_menu_options
        )
        if chosen_workspace_option == 1:
            print("Customer Management")
        elif chosen_workspace_option == 2:
            print("Employee Management")
        elif chosen_workspace_option == 3:
            print("Supplier Management")
        elif chosen_workspace_option == 4:
            print("Offerings")
        elif chosen_workspace_option == 5:
            print("Sales & Transactions")
        elif chosen_workspace_option == 6:
            print("Financial Management")
        elif chosen_workspace_option == 7:
            print("Reports")
        elif chosen_workspace_option == 8:
            print( "Analytics Centre")
        elif chosen_workspace_option == 9:
            print("Switch Client")
        elif chosen_workspace_option == 10:
            break

# ============================================= CLIENT MANAGEMENT ============================================

clients = []

industry_lists = {
    "Primary Sector (Extraction)": [
        "Agriculture & Farming",
        "Mining & Quarrying",
        "Fishing & Forestry"
    ],

    "Secondary Sector (Manufacturing & Construction)": [
        "Manufacturing",
        "Construction",
        "Energy & Utilities"
    ],

    "Tertiary Sector (Services)": [
        "Retail & Wholesale",
        "Hospitality & Tourism",
        "Financial & Insurance",
        "Healthcare & Social Assistance"
    ],

    "Quaternary Sector (Information & Knowledge)": [
        "Information Technology (IT) & Software",
        "Education & Training",
        "Research & Development (R&D)",
        "Media & Creative Services"

    ]
}

edit_menu = [
    "Client Name",
    "Client Phone Number",
    "Client Email",
    "Client Industry"
]

# business id generator
def generate_business_id(number):
    business_id = f"BUS-{number:04}"
    return business_id


def get_name():
    name = input(f"Enter Company Name: ").strip().title()
    return name

def get_number():
    while True:
            
            phone_input = input("Enter phone number: ")
            if not phone_input.isdigit(): 
                print("Please enter a valid number.")
                continue
            if len(phone_input) != 10:
                print("Enter only 10 digits.")
                continue
            phone_number = phone_input
            return phone_number

def get_email():
    while True:
            
            email_address = input("Enter email address: ")
            if email_address.count("@") != 1:
                print("Please enter a valid email format, (only one @)")
                continue
            if not email_address.endswith(".com"):
                print("Invalid Entry")
                continue
            return email_address

    
# choose industry
def choose_industry():
    while True:

        sector_names = list(industry_lists.keys())
        display_menu(
            "INDUSTRY SECTORS",
            sector_names
        )

        chosen_sector = get_menu_choice(
            "Choose your industry sector: ",
            sector_names
        )
    
        sector_name = sector_names[chosen_sector - 1]
        industry_sector = industry_lists[sector_name]

        display_menu(
            "INDUSTRIES",
            industry_sector
        )
        industry_option = get_menu_choice(
            "Choose your industry: ",
            industry_sector
        ) 

        chosen_industry_option = industry_sector[industry_option - 1]
        return chosen_industry_option
        

next_number = 1
def register_client():
    global next_number

    client_id = generate_business_id(next_number)
    client_name = get_name()
    phone_number = get_number()
    email_address = get_email()
    industry = choose_industry()

    client = {
        "client_id": client_id,
        "client_name": client_name,
        "client_phone": phone_number,
        "client_email": email_address,
        "industry": industry
    }
    clients.append(client)

    next_number += 1

def display_client(client):
        print(f"ID: {client['client_id']}")
        print(f"Name: {client['client_name']}")
        print(f"Phone: {client['client_phone']}")
        print(f"Email: {client['client_email']}")
        print(f"Industry: {client['industry']}")
        print("-" * 50)

def view_clients():
    if len(clients) == 0:
        print("No clients registered.")
    else:
        print("=" * 50)
        print("CLIENTS LIST",)
        print("=" * 50)
        for client in clients:
            display_client(client)
            
def find_client():
    client_number = int(input("Enter Client Number: "))
    search = f'BUS-{client_number:04}'

    for client in clients:
        if client['client_id'] == search:
            return client
    return None
        
def search_client():
    client = find_client()
    if client:
        print("=" * 50)
        print("SEARCH RESULT:",)
        print("=" * 50)
        display_client(client)
    else:
        print("Client not found.")

def edit_client():
    client = find_client()
    if client:
        display_menu(
            "EDIT OPTIONS:",
            edit_menu
        )
        chosen_edit_option = get_menu_choice(
            "What would you like to edit?",
            edit_menu
        )
        if chosen_edit_option == 1:
            client["client_name"] = get_name()
        elif chosen_edit_option == 2:
            client["client_phone"] = get_number()
        elif chosen_edit_option == 3:
            client["client_email"] = get_email()
        elif chosen_edit_option == 4:
            client["industry"] = choose_industry()
        print("Client updated successfully.")

    else:
        print("Client not found.")

def delete_client():
    client = find_client()
    
    if client:
        print(f" Deleting {client['client_name']} (no:{client['client_id']})")
        clients.remove(client)
        print(f"Client (no:{client['client_id']}) deleted sucessfully.")
    else:
        print("Client not found.")
# ============================================= CALLS ============================================
main()

