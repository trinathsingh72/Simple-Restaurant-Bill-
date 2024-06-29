class RestaurantBilling:
    def __init__(self):
        # Menu items
        self.menu = {
            1: {"item": "Paneer Butter Masala", "price": 250},
            2: {"item": "Chicken Biryani", "price": 200},
            3: {"item": "Vegetable Pulao", "price": 150},
            4: {"item": "Dal Tadka", "price": 120},
            5: {"item": "Butter Naan", "price": 40},
            6: {"item": "Masala Dosa", "price": 80},
            7: {"item": "Gulab Jamun", "price": 60},
            8: {"item": "Lassi", "price": 50},
            9: {"item": "Water", "price": 22},
        }
        self.order = []


    def show_menu(self):
        print("Menu:")
        for number, details in self.menu.items():
            print(f"{number}. {details['item']} - ₹{details['price']}")

    def take_order(self):
        while True:
            try:
                item_number = int(input("Enter the item number to order (0 to finish): "))
                if item_number == 0:
                    break
                if item_number in self.menu:
                    quantity = int(input(f"Enter quantity for {self.menu[item_number]['item']}: "))
                    self.order.append((item_number, quantity))
                else:
                    print("Invalid item number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

            

    def calculate_bill(self):
        total = 0
        print("\nYour Order:")
        for item_number, quantity in self.order:
            item = self.menu[item_number]['item']
            price = self.menu[item_number]['price']
            cost = price * quantity
            total += cost
            print(f"{item} (₹{price} x {quantity}) = ₹{cost}")
        print(f"\nTotal Bill: ₹{total}")

if __name__ == "__main__":
    billing_system = RestaurantBilling()
    billing_system.show_menu()
    billing_system.take_order()
    billing_system.calculate_bill()
