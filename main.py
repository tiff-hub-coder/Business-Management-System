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
            print("Please enter a valid number")
            continue
        if choice < 1 or choice > len(menu_options):
            print("Invalid Entry")
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
            print("Register Client")
        elif chosen_admin_option == 2:
            print("View Clients")
        elif chosen_admin_option == 3:
            print("Search Client")
        elif chosen_admin_option == 4:
            print("Edit Clients")
        elif chosen_admin_option == 5:
            print("Delete Client")    
        elif chosen_admin_option == 6:
            print("Save")
        elif chosen_admin_option == 7:
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

# ============================================= CALL FUNCTIONS ============================================
main()