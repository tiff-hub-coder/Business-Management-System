# ============================================= HELPER FUNCTIONS============================================
# ====== DISPLAY MENU FUNCTION ======
active_client = None

def activate_client_workspace():
        client = find_client()
        if not client:
            print("Client not found.\n Returning to main menu.")
        else:
            global active_client 
            active_client = (f"{client['id']} | {client['name']}")
            print(f"Business: {client['name']}")
            print(f"Owner: {client['owner']}")
            print(f"Industry: {client['industry']}")
            print(f"Business Type: {client['type']}")
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

def get_name(prompt, name_type):
    name_input = input(prompt).strip()
    if name_type == "person":
        name = name_input.title()
    elif name_type == "business":
        name = name_input
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
    "Name",
    "Phone Number",
    "Email",
    "Industry"
]

def edit_record(records, prefix, prompt, name_type):
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
            record["name"] = get_name(prompt, name_type)
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
    
# ====== RETURN TO MAIN FUNCTION ======

def should_exit():
    return True
while True:
    result = should_exit()
    if result:
        break
    print("Returning to main menu...")
print("Main menu loading...")

def return_to_main():
    print("Returning to main menu...")
    return True

# ====== ADMIN HELPER FUNCTION ======

def admin_menu(title, menu, prompt1, prompt2, records, prefix, display_function, add_function, name_type):
    while True:
        display_menu(
            title,
            menu
        )
        chosen_option = get_menu_choice(
            prompt1,
            menu
        )
        menu_actions = {
            1: add_function,
            2: lambda: view_records(records, title, display_function),
            3: lambda: search_record(records, prefix),
            4: lambda: edit_record(records, prefix, prompt2, name_type),
            5: lambda: delete_record(records, prefix),
            6: save_option,
            7: return_to_main
            }
        action = menu_actions[chosen_option]
        should_exit = action()
        if should_exit:
            break

# ====== EXIT FUNCTION ======

def exit_option():
    print("Exiting program...")
    return True

# ============================================= CLIENT ADMIN MENU ============================================
business_menu_options = [
    "Register Client",
    "View Clients",
    "Search Client",
    "Edit Client",
    "Delete Client",
    "Save",
    "Return to Main Menu"
]

def business_admin_menu():
    admin_menu("CLIENT ADMINISTRATION",
                business_menu_options,
                "Choose an administration option: ",
                "Enter new name: ",
                clients,
                "BUS-",
                display_client,
                add_client,
                "business"

               )

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

def add_client():
    global client_next_number

    client_id = generate_id("BUS-",client_next_number)
    client_name = get_name("Enter Business Name: ", "business")
    owner_name = get_name("Enter Owner Name: ", "person")
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
    return edit_record(clients, "BUS-", "Enter the business name: ", "business")

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
        workspace_actions ={
            1: customer_admin_menu,
            2: employee_admin_menu,
            3: supplier_admin_menu,
            4: print("Offerings"),
            5: print("Sales & Transactions"),
            6: print("Financial Management"),
            7: print("Reports"),
            8: print( "Analytics Centre"),
            9: print("Switch Client"),
            10: return_to_main
            }
        action = workspace_actions[chosen_workspace_option]
        should_exit = action()
        if should_exit:
            break

# ============================================= CUSTOMER MANAGEMENT ==============================

customer_menu_options = [
    "Add New Customer",
    "View Customers",
    "Search Customer",
    "Edit Customer",
    "Delete Customer",
    "Save",
    "Return to Main Menu"
]
customers = []

def customer_admin_menu():
    admin_menu(
    "CUSTOMER ADMINISTRATION",
    customer_menu_options,
    "Choose a customer workspace option: ",
    "Enter new name: ",
    customers,
    "CUS-",
    display_customer,
    add_customer,
    "person"
    )

customer_next_number = 1

def add_customer():
    global customer_next_number
    
    customer_id = generate_id("CUS-",customer_next_number)
    customer_name = get_name("Enter customer name: ", "person")
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

# ============================================= EMPLOYEE MANAGEMENT ==============================

employee_menu_options = [
    "Add New Employee",
    "View Employees",
    "Search Employee",
    "Edit Employee",
    "Delete Employee",
    "Save",
    "Return to Main Menu"
]
employees = []

def employee_admin_menu():
    admin_menu(
    "EMPLOYEE ADMINISTRATION",
    employee_menu_options,
    "Choose an employee workspace option: ",
    "Enter new name: ",
    employees,
    "EMP-",
    display_employee,
    add_employee,
    "person"
    )

def get_employee_salary():
    while True:
        try:
            salary = float(input("Enter employee's salary: "))
        except ValueError:
                print("Please enter a valid number.")
                continue
        employee_salary = round((salary), 2)
        return employee_salary

employee_next_number = 1

def add_employee():
    global employee_next_number
    
    employee_id = generate_id("EMP-",employee_next_number)
    employee_name = get_name("Enter employee name: ", "person")
    employee_phone = get_number()
    employee_email = get_email()
    employee_role = get_name("Enter employee's job title: ", "business")
    employee_salary = get_employee_salary()

    
    employee = {
        "id": employee_id,
        "name": employee_name,
        "phone": employee_phone,
        "email": employee_email,
        "role": employee_role,
        "salary": employee_salary
        }
    add_record(employees, employee)
    
    employee_next_number += 1

def display_employee(employee):
    display_record(employee)
    print(f"Role: {employee['role']}")
    print(f"Salary: R{employee['salary']:,.2f}")
    print("-" * 50)
 
# ============================================= SUPPLIER ADMIN ===================================

supplier_menu_options = [
    "Add New Supplier",
    "View Supplier",
    "Search Supplier",
    "Edit Supplier",
    "Delete Supplier",
    "Save",
    "Return to Main Menu"
]
suppliers = []

def supplier_admin_menu():
    admin_menu(
        "SUPPLIER ADMINISTRATION",
        employee_menu_options,
        "Choose a supplier workspace option: ",
        "Enter new name: ",
        suppliers,
        "SUP-",
        display_supplier,
        add_supplier,
        "business"
        )

def get_supplier_price():
    while True:
        try:
            price_per_unit = float(input("Enter the product's price per unit: "))
        except ValueError:
                print("Please enter a valid number.")
                continue
        price = round((price_per_unit),2)
        return price

supplier_next_number = 1

def add_supplier():
    global supplier_next_number
    
    supplier_id = generate_id("SUP-",supplier_next_number)
    supplier_name = get_name("Enter suppliers name: ", "business")
    supplier_phone = get_number()
    supplier_email = get_email()
    supplier_product = get_name("Enter product name: ", "business")
    supplier_price = get_supplier_price()

    
    supplier = {
        "id": supplier_id,
        "name": supplier_name,
        "phone": supplier_phone,
        "email": supplier_email,
        "product": supplier_product,
        "price": supplier_price
        }
    add_record(suppliers, supplier)
    
    supplier_next_number += 1

def display_supplier(supplier):
    display_record(supplier)
    print(f"Role: {supplier['product']}")
    print(f"Price: R{supplier['price']:,.2f}")
    print("-" * 50)

# ============================================= MAIN MENU ============================================

main_menu_options = [
    "Client Administration",
    "Open Client Workspace",
    "Save Data",
    "Exit"
]
# ============================================= MAIN FUNCTION ============================================

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

        main_actions = {
            1: business_admin_menu,
            2: activate_client_workspace,
            3: save_option,
            4: exit_option
        }
        action = main_actions[chosen_main_option]
        should_exit = action()
        if should_exit:
            break
main()