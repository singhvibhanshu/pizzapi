from pizzapy import Customer, StoreLocator

customer = Customer("Vibhanshu", "Singh", "singhvibhanshu@hotmail.com", "9999999999", "MIG 64, Toronto, ON, M5J2X2")

my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)

print("\nMENU\n")

menu = my_local_dominos.get_menu()

def searchMenu(menu):
    print("You are now searching the menu.")
    while True:
        item = input("Type an item to look for: ").strip().lower()

        if len(item) > 1:
            item = item[0].upper() + item[1:]
        else:
            print("Invalid input. Exiting the search.")
            break

        print(f"Results for: {item}")
        menu.search(Name=item)

searchMenu(menu)