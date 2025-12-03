# This module should implement filtering using Dictionary Comprehensions
def filter_customers_by_city(self, city):
        """Placeholder for filtering customers (students will implement)."""
        filtered_customers = {cust_id: details for cust_id, details in self.customers.items() if details["location"].lower() == city.lower()}
    
        if filtered_customers:
            print(f"\nCustomers in {city}:")
            self.display_customers(filtered_customers)
        else:
            print(f"\nNo customers found in {city}.")