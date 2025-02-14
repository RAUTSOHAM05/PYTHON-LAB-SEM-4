
class Product:
    def __init__(self, name, price, stock_quantity):       # Initialize product with name, price, and stock quantity
        self.name = name    # Product's name
        self.price = price      # Product's price
        self.stock_quantity = stock_quantity    # Quantity available in stock

    # Method to update the stock quantity 
    def update_stock(self, quantity):
        self.stock_quantity += quantity  # Increase or decrease stock 

    # Method to get the details of the product 
    def get_details(self):
        return f"Name: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock_quantity}"

class Store:
    def __init__(self):
        self.products = {}  # Dictionary to store products 
   
    def add_product(self, name, price, stock_quantity):     # Method to add a new product to the store
        if name not in self.products:
            self.products[name] = Product(name, price, stock_quantity)
        else:
            print(f"Product {name} already exists!")

    # Method to update the stock of an existing product
    def update_product_stock(self, name, quantity):
        
        if name in self.products:
            self.products[name].update_stock(quantity)
        else:
            print(f"Product {name} not found!")     # If the product doesn't exist, notify the user

    # Method to view the details of a product
    def view_product_details(self, name):
        if name in self.products:          # Display the product if they exists
            print(self.products[name].get_details())
        else:
            print(f"Product {name} not found!")     #Product not in list 

# Main function that runs the store management system
def main():
    # Create an instance of Store
    store = Store()

    while True:
        # Display the main menu
        print("\nStore Management System")
        print("1. Add Product")
        print("2. Update Product Stock")
        print("3. View Product Details")
        print("4. Exit")

        # Take user's choice as input
        choice = input("Enter your choice: ")

        # Add a new product
        if choice == "1":
            name = input("Enter product name: ") 
            price = float(input("Enter product price: "))  
            stock_quantity = int(input("Enter product stock quantity: "))  
            store.add_product(name, price, stock_quantity)  

        # Update stock of an existing product
        elif choice == "2":
            name = input("Enter product name to update stock: ")  
            quantity = int(input("Enter quantity to add/remove: "))  
            store.update_product_stock(name, quantity)  

        #  View details of a specific product
        elif choice == "3":
            name = input("Enter product name to view details: ")  
            store.view_product_details(name)  

        # Exit the system
        elif choice == "4":
            print("Exiting the system. Goodbye!")  
            break  

        else:
            print("Invalid choice. Please try again.")  # Error message for invalid choice

# If this script is executed directly (not imported), call the main function
if __name__ == "__main__":
    main()
