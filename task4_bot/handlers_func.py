from prettytable import PrettyTable


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return str(e)
    return wrapper


def add_contact(args, contacts):
    """User adding"""
    if len(args) < 2:
        raise ValueError("Give me name and phone please")
    name, phone_number = args
    contacts[name] = phone_number
    return f"Contact added."

@input_error
def change_contact(args, contacts):
    """Changing the phone number by user name"""
    if len(args) < 2:
        raise ValueError("Give me name and phone please")
    name, phone_number = args
    if name in contacts:
        contacts[name] = phone_number
    else:
        return f"User not found"
    return f"Contact updated."

@input_error
def show_phone(args, contacts):
    """Display user phone number by name"""

    if len(args) < 1:
        raise ValueError("Give me name please")
    name = args[0]
    if name in contacts:
        phone_number = contacts[name]
        return f"Your phone number is: {phone_number}"
    else:
        return f"User not found"

@input_error
def show_all_contacts(contacts):
    """Display information about all users"""
    table = PrettyTable()
    table.field_names = ["Name", "Phone Number"]
    for name, phone_number in contacts.items():
        table.add_row([name, phone_number])
    print(f"All users information:\n{table}")