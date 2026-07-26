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
def display_main_menu():
    print("\n" + "=" * 50)
    print(f'BUSINESS MANAGEMENT & ANALYTICS SYSTEM')
    print("=" * 50)
    print(f'Active Client: ')
    print("None")
    print('='* 50)
    for number, option in enumerate(main_menu_options, start = 1):
        print(f' {number}.{option}')

def get_choice():
    main_menu_choice = int(input(f'Enter your choice: '))
    while main_menu_choice < 1 or main_menu_choice > len(main_menu_options):
        print("Invalid Entry")
        display_main_menu()
        main_menu_choice = int(input(f'Enter your choice: '))
    return main_menu_choice

def display_client_admin():
    print("\n" + "=" * 30)
    print("=" * 30)
    print(f'Active Client: ')
    print("None")
    print("=" * 30)
    for number, option in enumerate(admin_menu_options, start = 1):
        print(f' {number}.{option}')

def display_workspace():
    print("\n" + "=" * 30)
    print("=" * 30)
    print(f'Active Client: ')
    print("None")
    print("=" * 30)
    for number, option in enumerate(workspace_menu_options, start = 1):
        print(f' {number}.{option}')

def get_admin_choice():
    admin_menu_choice = int(input(f'Enter an administration option: '))
    while admin_menu_choice < 1 or admin_menu_choice > len(admin_menu_options):
        print("Invalid Entry")
        display_client_admin()
        admin_menu_choice = int(input(f'Enter an administration option: '))
    return admin_menu_choice

def get_workspace_choice():
    workspace_menu_choice = int(input(f'Enter a workspace option: '))
    while workspace_menu_choice < 1 or workspace_menu_choice > len(workspace_menu_options):
        print("Invalid Entry")
        display_workspace()
        workspace_menu_choice = int(input(f'Enter a workspace option: '))
    return workspace_menu_choice

def save_option():
    print("Save feature coming in Version 3.")

def exit_option():
    print("Exiting...")


def main():
    while True:
        display_main_menu()
        chosen_main_option = get_choice()

        if chosen_main_option == 1:
            admin_menu()
        elif chosen_main_option == 2:
            display_workspace()
            chosen_workspace_option = get_workspace_choice()
        elif chosen_main_option == 3:
            save_option()
        elif chosen_main_option == 4:
            exit_option()
            break

def admin_menu():

    while True:
        display_client_admin()
        chosen_admin_option = get_admin_choice()

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


main()