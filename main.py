# ============================================= MAIN MENU ============================================

main_menu_options = [
    "Client Administration",
    "Open Client Workspace",
    "Save Data",
    "Exit"
]

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
            activate_client_workspace()
        elif chosen_main_option == 3:
            save_option()
        elif chosen_main_option == 4:
            exit_option()
            break

# ============================================= HELPER FUNCTIONS============================================
# ====== DISPLAY MENU FUNCTION ======
active_client = None

def activate_client_workspace():
        client = find_client()
        if not client:
            print("Client not found.\n Returning to main menu.")
        else:
            global active_client 
            active_client = (f'{client['id']} | {client['name']}')
            print(f'Business: {client['name']}')
            print(f'Owner: {client['owner']}')
            print(f"Industry: {client['industry']}")
            print(f'Business Type: {client['type']}')
            print("Loading Workspace...")
            workspace_menu()
    
def display_menu(title, menu_options):

    print("=" * 50)
    print(title)
    print("=" * 50)
    print(f"Active Client: {active_client}")
    print("=" * 50)

    for number, option in enumerate(menu_options, start=1):
        print(f"{number}. {option}")

# ====== GET CHOICE FUNCTION ======

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

# ====== SAVE FUNCTION ======

def save_option():
    print("Save feature coming in Version 3.")

# ====== EXIT FUNCTION ======

def exit_option():
    print("Exiting...")

# ============= INFORMATION MANAGEMENT FUNCTIONS =============

# ====== ID GENERATOR FUNCTION ======

def generate_id(prefix, number):
    id = f"{prefix}{number:04}"
    return id

# ====== GET DETAILS FUNCTIONS ======

def get_name(prompt):
    name = input(f"{prompt}").strip().title()
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

# ====== APPEND RECORDS FUNCTION ======

def add_record(records, record):
    records.append(record)

# ====== FIND RECORD FUNCTIONS ======

def find_record(records, prefix):
    while True:
        try:
            record_number = int(input("Enter ID Number: "))
            break
        except ValueError:
            print("Please enter a valid ID number.")

    search = f'{prefix}{record_number:04}'
    for record in records:
        if record['id'] == search:
            return record   
    return None
        
def search_record(records, prefix):
    searched_record = find_record(records, prefix)
    if searched_record:
        print("=" * 50)
        print("SEARCH RESULT:",)
        print("=" * 50)
        display_client(searched_record)
    else:
        print("Record not found.")

# ====== EDIT FUNCTION ======

edit_menu = [
    "Client Name",
    "Client Phone Number",
    "Client Email",
    "Client Industry"
]

def edit_record(records, prefix):
    record = find_record(records, prefix)
    if record:
        display_menu(
            "EDIT OPTIONS:",
            edit_menu
        )
        chosen_edit_option = get_menu_choice(
            "What would you like to edit?",
            edit_menu
        )
        if chosen_edit_option == 1:
            record["name"] = get_name()
        elif chosen_edit_option == 2:
            record["phone"] = get_number()
        elif chosen_edit_option == 3:
            record["email"] = get_email()
        elif chosen_edit_option == 4:
            record["industry"] = choose_industry()
        print("Record updated successfully.")

    else:
        print("Record not found.")

def delete_record(records, prefix):
    record = find_record(records, prefix)
    
    if record:
        print(f" Deleting {record['name']} (no:{record['id']})")
        records.remove(record)
        print(f"Client (no:{record['id']}) deleted sucessfully.")
    else:
        print("Record not found.")

# ====== DISPLAY FUNCTIONS ======

def display_record(record):
        print(f"ID: {record['id']}")
        print(f"Name: {record['name']}")
        print(f"Phone: {record['phone']}")
        print(f"Email: {record['email']}")
        print("-" * 50)

def view_records(records, title, display_function):

    if len(records) == 0:
        print("No records found.")
        return

    print("=" * 50)
    print(title)
    print("=" * 50)

    for record in records:
        display_function(record)

# ====== STATUS FUNCTION ======

def status_check():
    while True:
        status = input("Is customer a registered loyalty member?y/n ").strip().lower()
        if status not in ("yes", "no"):
            print("Enter Yes or No?")
            continue
        if status == "yes":
            status = True
        else:
            status = False
        return status

# ============================================= ADMIN MENU ============================================
admin_menu_options = [
    "Register Client",
    "View Clients",
    "Search Client",
    "Edit Client",
    "Delete Client",
    "Save",
    "Return to Main Menu"
]

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
            view_records(clients, "CLIENTS", display_client)
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

business_types = [
    "Merchandising",
    "Service",
    "Hybrid"
]       

def get_business_type():
    while True:
        display_menu("Business Types", business_types)
        type_choice = get_menu_choice("Choose Business Type:", business_types)
        chosen_type = business_types[type_choice - 1]
        return chosen_type

client_next_number = 1

def register_client():
    global client_next_number

    client_id = generate_id("BUS-",client_next_number)
    client_name = get_name("Enter Business Name: ")
    owner_name = get_name("Enter Owner Name: ")
    phone_number = get_number()
    email_address = get_email()
    business_type = get_business_type()
    industry = choose_industry()

    client = {
        "id": client_id,
        "name": client_name,
        "owner": owner_name,
        "phone": phone_number,
        "email": email_address,
        "industry": industry,
        "type": business_type
    }
    add_record(clients, client)

    client_next_number += 1

def display_client(client):
    display_record(client)
    print(f'Owner: {client['owner']}')
    print(f"Industry: {client['industry']}")
    print(f'Business Type: {client['type']}')
    print("-" * 50)

def find_client():
    return find_record(clients, "BUS-")
        
def search_client():
    return search_record(clients, "BUS-")

def edit_client():
    return edit_record(clients, "BUS-")

def delete_client():
    delete_record(clients, "BUS-")

# ============================================= WORKSPACE MENU ============================================
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
            customer_admin_menu()
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

# ============================================= CUSTOMER MANAGEMENT ==============================

customer_menu_options = [
    "Add New Customer",
    "View Customers",
    "Search Customers",
    "Edit Customers",
    "Delete Customers",
    "Save",
    "Return to Main Menu"
]
customers = []

def customer_admin_menu():
    while True:
        display_menu(
            "CUSTOMER ADMINISTRATION",
            customer_menu_options
        )
        chosen_customer_option = get_menu_choice(
            "Choose a workspace option: ",
            customer_menu_options
        )
        if chosen_customer_option == 1:
            add_customer()
        elif chosen_customer_option == 2:
            view_records(customers, "CUSTOMERS", display_customer)
        elif chosen_customer_option == 3:
            search_record(customers, "CUS-")
        elif chosen_customer_option == 4:
            edit_record(customers, "CUS-")
        elif chosen_customer_option== 5:
            delete_record(customers, "CUS-")
        elif chosen_customer_option == 6:
            save_option()
        elif chosen_customer_option == 7:
            exit_option()
            break

customer_next_number = 1

def add_customer():
    global customer_next_number
    
    customer_id = generate_id("CUS-",customer_next_number)
    customer_name = get_name("Enter Customer Name: ")
    customer_phone = get_number()
    customer_email = get_email()
    loyalty_membership = status_check()

    
    customer = {
        "id": customer_id,
        "name": customer_name,
        "phone": customer_phone,
        "email": customer_email,
        "membership": loyalty_membership
        }
    add_record(customers, customer)
    
    customer_next_number += 1

def display_customer(customer):
    display_record(customer)
    print(f"Membership: {customer['membership']}")
    print("-" * 50)




# ============================================= CALLS ============================================
main()

