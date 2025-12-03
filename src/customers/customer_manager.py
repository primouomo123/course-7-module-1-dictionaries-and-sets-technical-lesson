class CustomerManager:
    def __init__(self, customers):
        self.customers = customers

    def display_customers(self, customers=None):
        """Displays all customer records."""
        print("\nCustomer Records:")
        if customers is None:
            customers = self.customers
        for cust_id, details in customers.items():
            print(f"ID: {cust_id} | Name: {details['name']} | Location: {details['location']} | Purchases: {details['purchases']}")

def update_customer_location(self, customer_id, new_location):
    if customer_id in self.customers:
        old_location = self.customers[customer_id]['location']
        self.customers[customer_id]['location'] = new_location
        print(f"\nUpdated {self.customers[customer_id]['name']}'s location from {old_location} to {new_location}.")
    else:
        print(f"\nCustomer not found")