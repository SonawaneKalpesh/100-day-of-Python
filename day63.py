inventory = {}

while True:
    print("\n===== INVENTORY MENU =====")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Search Product")
    print("4. Delete Product")
    print("5. View Inventory")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        inventory[product] = quantity
        print("Product added successfully!")

    elif choice == "2":
        product = input("Enter product name: ")

        if product in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[product] = quantity
            print("Product updated successfully!")
        else:
            print("Product not found.")

    elif choice == "3":
        product = input("Enter product name: ")

        if product in inventory:
            print(f"{product} : {inventory[product]}")
        else:
            print("Product not found.")

    elif choice == "4":
        product = input("Enter product name: ")

        if product in inventory:
            del inventory[product]
            print("Product deleted successfully!")
        else:
            print("Product not found.")

    elif choice == "5":
        if inventory:
            print("\n--- Inventory ---")
            for product, quantity in inventory.items():
                print(f"{product} : {quantity}")
        else:
            print("Inventory is empty.")

    elif choice == "6":
        print("Exiting Inventory System...")
        break

    else:
        print("Invalid choice. Try again.")